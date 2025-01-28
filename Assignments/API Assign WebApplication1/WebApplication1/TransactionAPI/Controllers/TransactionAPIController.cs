using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;
using TransactionAPI.Models;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace TransactionAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class TransactionAPIController : ControllerBase
    {
        TransDbContext context;

        public TransactionAPIController(TransDbContext context)
        {
            this.context = context; 
        }
        // GET: api/<TransactionAPIController>
        [HttpGet]
        public ActionResult Get()
        {
            List<Transaction> transactions = context.Transactions.ToList();
            if (transactions == null)
            {
                return NotFound("No Data");
            }
            else
            {

                return Ok(transactions);
            }
        }

        // GET api/<TransactionAPIController>/5
        [HttpGet("{id}")]
        public ActionResult Get(int id)
        {
            Transaction transaction = context.Transactions.Find(id);
            if (transaction == null)
            {
                return NotFound("No Transaction Found");
            }
            else
            {
                return Ok(transaction);
            }
            

            
        }

        

        // POST api/<TransactionAPIController>
        [HttpPost]
        public ActionResult Post([FromBody] Transaction transaction)
        {
            decimal processedAmount = 0;

            if (transaction.CurrencyInHand == "USD" && transaction.CurrencyRequest
                == "INR")
            {
                processedAmount = 86.75M * transaction.AmountInHand;
            }
            if (transaction.CurrencyInHand == "EUR" && transaction.CurrencyRequest
                == "INR")
            {
                processedAmount = 93.88M * transaction.AmountInHand;
            }
            if (transaction.CurrencyInHand == "USD" && transaction.CurrencyRequest
                == "EUR")
            {
                processedAmount =  transaction.AmountInHand/ 0.012M ;
            }
            if (transaction.CurrencyInHand == "INR" && transaction.CurrencyRequest
                == "USD")
            {
                processedAmount = transaction.AmountInHand / 86.75M;
            }
            if (transaction.CurrencyInHand == "INR" && transaction.CurrencyRequest
                == "EUR")
            {
                processedAmount = transaction.AmountInHand / 93.88M;
            }
            if (transaction.CurrencyInHand == "EUR" && transaction.CurrencyRequest
                == "USD")
            {
                processedAmount = 0.012M* transaction.AmountInHand ;
            }
            transaction.ProcessedAmount = processedAmount;
            context.Transactions.Add(transaction);
            int result=context.SaveChanges();
            if (result > 0)
            {
                return Ok("Transaction Successfull");
            }
            else
            {

                return BadRequest("Transaction Failed");
            }
        }

        // PUT api/<TransactionAPIController>/5
        [HttpPut("{id}")]
        public ActionResult Put(int id, [FromBody] Transaction transaction)
        {
            decimal processedAmount = 0;
            Transaction transaction1 = context.Transactions.Find(id);
            if (transaction1 == null)
            {
                return NotFound("No Transaction Found, MOdification Failed");
            }

            if (transaction1.CurrencyInHand == "USD" && transaction1.CurrencyRequest
                == "INR")
            {
                processedAmount = 86.75M * transaction1.AmountInHand;
            }
            if (transaction1.CurrencyInHand == "EUR" && transaction1.CurrencyRequest
                == "INR")
            {
                processedAmount = 93.88M * transaction1.AmountInHand;
            }
            if (transaction1.CurrencyInHand == "USD" && transaction1.CurrencyRequest
                == "EUR")
            {
                processedAmount = transaction1.AmountInHand / 0.012M;
            }
            if (transaction1.CurrencyInHand == "INR" && transaction1.CurrencyRequest
                == "USD")
            {
                processedAmount = transaction1.AmountInHand / 86.75M;
            }
            if (transaction1.CurrencyInHand == "INR" && transaction1.CurrencyRequest
                == "EUR")
            {
                processedAmount = transaction1.AmountInHand / 93.88M;
            }
            if (transaction1.CurrencyInHand == "EUR" && transaction1.CurrencyRequest
                == "USD")
            {
                processedAmount= 0.012M * transaction1.AmountInHand;
            }


            transaction1.ProcessedAmount = processedAmount;
            transaction1.CustomerName = transaction.CustomerName;
            transaction1.CurrencyRequest = transaction1.CurrencyRequest;
            transaction1.CurrencyInHand = transaction1.CurrencyInHand;
            transaction1.AmountInHand = transaction1.AmountInHand;
            //transaction1.ProcessedAmount = transaction1.ProcessedAmount;
            int result = context.SaveChanges();
            if (result > 0)
            {
                return Ok("Update Sucessfull");
            }
            else
            {
                return BadRequest("Not Updated, Incorrect Id Or Wrong Input! ");
            }

        }

        // DELETE api/<TransactionAPIController>/5
        [HttpDelete("{id}")]
        public ActionResult Delete(int id)
        {
            Transaction transaction = context.Transactions.Find(id);
            if (transaction == null)
            {
                return NotFound("No Transaction Found");
            }
            context.Transactions.Remove(transaction);
            int result = context.SaveChanges();
            if (result>0)
            {
                return Ok("Deleted Successfully");
            }
            else
            {
                return BadRequest("Not Deleted, Incorrect Id !");
            }
        }
    }
}
