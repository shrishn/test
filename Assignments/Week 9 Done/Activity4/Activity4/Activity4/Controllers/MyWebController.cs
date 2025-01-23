using Microsoft.AspNetCore.Mvc;

namespace Activity4.Controllers
{
    public class MyWebController : Controller
    {
        public IActionResult Greetings(string id)
        {
            if (string.IsNullOrEmpty(id))
            {
                return Content("Hello World");
            }
            else
            {
                return Content($"Hello {id}");
            }
        }
    }
}
