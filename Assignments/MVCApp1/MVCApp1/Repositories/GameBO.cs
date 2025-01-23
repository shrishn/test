using MVCApp1.Models;
using System.Diagnostics;

namespace MVCApp1.Repositories
{
    public class GameBO : IRepository<Game>
    {
        SportsDbContext context;
        public GameBO(SportsDbContext context) //Dependency injection through constructor --> when GameBO is called, SportsDbContext db is invoked automatically
        //using controller reference
        {
            this.context = context;
        }
        public bool Add(Game entity)
        {
            try
            {
                context.Game.Add(entity);
                int r = context.SaveChanges();
                if (r > 0)
                {
                    return true;
                }
                return false;
            }

            catch (Exception ex)
            {
                Debug.WriteLine("################" + ex.Message);
                return false;
            }
        }

        public List<Game> GetAllDetails()
        {
            return context.Game.ToList();
        }

        public bool Modify(Game entity)
        {
            Game game=context.Game.Find(entity.GameId);
            game.Name=entity.Name;
            game.GameType=entity.GameType;
            int r = context.SaveChanges();
            if (r > 0)
            {
                return true;
            }
            return false;

        }

        public bool Remove(Game entity)
        {
            context.Game.Remove(entity);
            int r=context.SaveChanges();
            if (r > 0)
            {
                return true;
            }
            return false;
        }

        public Game Search(object Id)
        {
            int gameId = (int)Id;
            Game game=context.Game.Find(gameId);
            return game;
        }
    }
}
