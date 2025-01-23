using Microsoft.EntityFrameworkCore;

namespace TransactionAPI.Models
{
    public class TransDbContext : DbContext {

        public TransDbContext(DbContextOptions<TransDbContext> options) : base(options)
        {
        }

        public virtual DbSet<Transaction> Transactions { get; set; }

    }
}
