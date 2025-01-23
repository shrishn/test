using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConAppEFCode1.Models
{
    public class OrganizationContext:DbContext
    {
        public OrganizationContext() 
        { 
            //no argument constructor
        }

        protected override void OnConfiguring(DbContextOptionsBuilder dbco)
        {
            base.OnConfiguring(dbco);   //takes care of building connections

            string constring = ConfigurationManager.ConnectionStrings["sqlcon"].ConnectionString;

            dbco.UseSqlServer(constring);
        }

        
        public virtual DbSet<Department> Departments { get; set; }
        public virtual DbSet<Employee> Employees { get; set; }

    }
}
