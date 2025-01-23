using Microsoft.EntityFrameworkCore;

namespace MVCApp1.Models
{
    public class SportsDbContext:DbContext
    {
        public SportsDbContext(DbContextOptions<SportsDbContext> options):base (options) 
        {
            //no argument constructor
        }
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            base.OnConfiguring(optionsBuilder);
        }

        //fluent api 
        protected override void OnModelCreating(ModelBuilder builder)
        {
            
            base.OnModelCreating(builder);
            builder.Entity<Player>().HasKey(p=>p.PlayerId); //configure player id in player instance as key instead of data anotation using fluent api extention method
            builder.Entity<Player>().Property(p => p.PlayerName).IsRequired().HasMaxLength(30);
            builder.Entity<Player>().Property(p=>p.Country).IsRequired().HasMaxLength(30);
            builder.Entity<Player>().Property(p => p.Age).IsRequired();

            //builder.Entity<Player>().HasData(
            //    new Models.Player[]
            //    {
            //        new Player(){PlayerId=716,Country="India",Gender=Gender.Male.ToString(),Age=24,PlayerName="Neeraj Chopra",GameId=1},
            //        new Player(){PlayerId=716,Country="India",Gender=Gender.Female.ToString(),Age=24,PlayerName="PT Usha",GameId=2}
            //    });

            builder.Entity<Game>().HasKey(g => g.GameId);
            builder.Entity<Game>().HasMany(g => g.Players).WithOne().HasForeignKey(p => p.GameId);

            builder.Entity<Game>().HasData(new Game[]
            {
                new Game(){GameId=1, Name="Javelin Throw",GameType="Individual"},
                new Game(){GameId=2,Name="Women's 400 M Race",GameType="Individual"},
                new Game(){GameId=3,Name="Long Jump",GameType="Individual"}
            });


            builder.Entity<GameEvent>().HasKey(ge=>ge.Id);
            builder.Entity<Performance>().HasKey(pf=>pf.SerialId);
        }
        public virtual DbSet<Player> Players { get; set; }   
        public virtual DbSet<Game> Game { get;set; }
        public virtual DbSet<GameEvent> GameEvent { get; set; }
        public virtual DbSet<Performance> Performance { get; set; }
    }
}
