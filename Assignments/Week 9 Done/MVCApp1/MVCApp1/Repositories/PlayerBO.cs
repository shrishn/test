using MVCApp1.Models;
using System.Diagnostics;

namespace MVCApp1.Repositories
{
    public class PlayerBO : IRepository<Player>
    {
        public SportsDbContext context;
        public PlayerBO(SportsDbContext context)
        {
            this.context = context; //dependency injection
        }
        public bool Add(Player entity)
        {
            try
            {
                context.Players.Add(entity);
                int r = context.SaveChanges();
                if (r > 0)
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
            catch (Exception ex)
            {
                Debug.WriteLine("################" + ex.Message);
                return false;
            }
        }

        public List<Player> GetAllDetails()
        {
            return context.Players.ToList();
        }

        public bool Modify(Player entity)
        {
            Player player = context.Players.Find(entity.PlayerId);
            player.PlayerName = entity.PlayerName;
            player.Country = entity.Country;
            player.Gender = entity.Gender;
            player.GameId = entity.GameId;
            player.Age = entity.Age;
            int r = context.SaveChanges();
            if (r > 0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        public bool Remove(Player entity)
        {
            context.Players.Remove(entity);
            int r = context.SaveChanges();
            if (r > 0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        public Player Search(object Id)
        {
            int playerId = (int)Id;
            Player player = context.Players.Find(playerId);
            return player;
        }
    }
}
