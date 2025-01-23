using Microsoft.AspNetCore.Mvc;
using System.Transactions;
using Newtonsoft.Json;
using System.Collections.Generic;
using System.Net.Http;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace TransactionMVC.Controllers
{
    public class TransactionController : Controller
    {
        [HttpGet]
        public IActionResult ProcessTransaction()
        {
            TransactionMVC.Models.Transaction trn = new TransactionMVC.Models.Transaction();
            return View(trn);
        }
        [HttpPost]
        public IActionResult ProcessTransaction(TransactionMVC.Models.Transaction transaction)
        {
            transaction.TransDate = DateTime.Now;
            HttpClient client = new HttpClient();
            client.BaseAddress = new Uri("https://localhost:7109");
            Task<HttpResponseMessage> response = client.PostAsJsonAsync<TransactionMVC.Models.Transaction>("/api/TransactionAPI", transaction);
            response.Wait();
            if (response.IsCompleted)
            {
                // Task<string> message = response.Result.Content.ReadFromJsonAsync<string>();
                // message.Wait();
                ViewBag.Message = "Details Submitted";
                return RedirectToAction("GetDetails");
            }
            return View("Error");
        }

        public IActionResult GetDetails()
        {
            HttpClient client = new HttpClient();
            client.BaseAddress = new Uri("https://localhost:7109");
            Task<List<TransactionMVC.Models.Transaction>> response = client.GetFromJsonAsync<List<TransactionMVC.Models.Transaction>>("/api/TransactionAPI");
            response.Wait();

            if (response.IsCompleted)
            {
                List<TransactionMVC.Models.Transaction> transData = response.Result;
                return View(transData);
            }
            return View("Error");
        }

        public IActionResult GetDetailsById(int id)
        {
            return View();
        }

    }
}