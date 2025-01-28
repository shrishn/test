using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;
using Newtonsoft.Json;

namespace TransactionMVC.Models
{
    public class Transaction
    {
        public int TransId { get; set; }
        public DateTime TransDate { get; set; }
        public string CustomerName { get; set; }
        public string CurrencyInHand { get; set; }
        public string CurrencyRequest { get; set; }
        public decimal AmountInHand { get; set; }
        public decimal ProcessedAmount { get; set; }

    }
}