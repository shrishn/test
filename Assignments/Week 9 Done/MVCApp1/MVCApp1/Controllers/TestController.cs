using Microsoft.AspNetCore.Mvc;
using MVCApp1.Models;
using MVCApp1.Repositories;

namespace MVCApp1.Controllers
{
    public class TestController : Controller
    {
        GameBO gameRepos;
        public TestController(SportsDbContext context) 
        { 
            gameRepos = new GameBO(context);
        }
        public List<Game> Index()
        {
            return gameRepos.GetAllDetails();
        }

        public Game SearchGame(int id)
        {
            return gameRepos.Search(id);

        }

        public String RemoveGame(int id)
        {
            Game game=gameRepos.Search(id);
            bool b=gameRepos.Remove(game);
            if (b)
            {
                return "Game Details is Removed";
            }
            return "Game Details is not Removed, Invalid Id";
        }

        public string AddGame(string gameName, string gameType)
        {

            Game game=new Game() { Name = gameName, GameType = gameType };
            bool b=gameRepos.Add(game);
            if (b)
            {
                return "Game details is inserted";
            }
            return "Game details is not inserted";
        }

        public string UpdateGame(int id, string gameName, string gameType)
        {
            Game game = gameRepos.Search(id);
            game.Name = gameName;
            game.GameType = gameType;
            bool b = gameRepos.Modify(game);
            if (b)
            {
                return "Game details is modified";
            }
            return "Game details is not modified";
        }
    }
}
