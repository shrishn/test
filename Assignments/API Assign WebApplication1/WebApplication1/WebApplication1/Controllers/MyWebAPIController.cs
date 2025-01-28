using Microsoft.AspNetCore.Mvc;
//using WebAPIApp.Models;
using WebAPIApp1.Models;

namespace WebAPIApp1.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class MyWebAPIController : Controller
    {
        /*public IActionResult Index()
        {
            return View();

        }*/

        public static List<Employee> employees = new List<Employee>();


        [HttpGet("Message1")]
        public string GetMessage()
        {
            return "Hello Users from Web Api Get Service";
        }
        [HttpPost]
        public ActionResult<string> PostEmpDetails([FromBody] Employee employee)
        {

            employees.Add(employee);
            return Ok("Employee added");

        }
        [HttpGet("Message2")]
        public string GetMessage2()
        {
            return "Hi from Web Api Get Service";
        }

        [HttpGet]
        public ActionResult<List<Employee>> GetEmployees()
        {
            return Ok(employees);
        }

        [HttpGet("{id}")]// get including linq and lambda

        public ActionResult<string> GetEMployee(int id)
        {
            Employee emplo = employees.Where(e => e.EmployeeId == id).FirstOrDefault();
            if (emplo == null)
            {
                return NotFound("Resource is not found");

            }
            return Ok(emplo);
        }
        /*
        [HttpPut]
        public ActionResult UpdateEmployee(int id, [FromBody] Employee employee)
        {
            Employee emplo = employees.Where(e => e.EmployeeId == id).FirstOrDefault();
            if (emplo == null)
            {
                return NotFound("not available");

            }
            emplo.Name = employee.Name;
            int index = 0;

            foreach (Employee emp in employees) {

                if (emplo.Id == id)
                {
                    break;

                }
                else
                {

                }
                index++;


            });
            return ("User updated");

        }*/
        [HttpPut("{id}")]
        public ActionResult UpdateEmployee(int id, [FromBody] Employee employee)
        {
            var existingEmployee = employees.FirstOrDefault(e => e.EmployeeId == id);
            if (existingEmployee == null)
            {
                return NotFound("Employee not available");
            }

            existingEmployee.Name = employee.Name;

            return Ok("User updated");
        }






        /*[HttpDelete("{id}")]
        public ActionResult DeleteEmployee(int id)
        {
            Employee emplo = employees.Where(e => e.EmployeeId == id).FirstOrDefault();
            if (emplo == null)
            {
                return NotFound("Resource is not found");

            }
            employees.Remove(emplo);
            return Ok(emplo);
        }
        */
        [HttpDelete("{id}")]
        public ActionResult DeleteEmployee(int id)
        {
            var employee = employees.FirstOrDefault(e => e.EmployeeId == id);
            if (employee == null)
            {
                return NotFound("Resource not found");
            }
            employees.Remove(employee);
            return Ok(employee);
        }

    }
}
