using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;
using Microsoft.EntityFrameworkCore.Metadata.Internal;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Security.Principal;
namespace TransactionAPI.Models
{
    public class Transaction
    {
        
        [Key, DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int TransId { get; set; }
        public DateTime TransDate { get; set; }
        public string CustomerName { get; set; }
        public string CurrencyInHand { get; set; }
        public string CurrencyRequest { get; set; }
        public decimal AmountInHand { get; set; }
        public decimal ProcessedAmount { get; set; }
    }
}
