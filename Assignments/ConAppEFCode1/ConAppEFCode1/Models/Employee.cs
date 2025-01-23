using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConAppEFCode1.Models
{
    public class Employee
    {
        [Key]
        public string EmpId { get; set; } //scalar property

        [Required, MaxLength(50)]
        public string Name { get; set; }

        [ForeignKey("Department")]
        public int WorkDeptId {  get; set; } // set navigation property as we have declared it as foreign key

        [Required]
        public long Salary { get; set; }

        //reference navigation property for work dept id
        public Department Department { get; set; }

        public ICollection<Employee> Employees { get; set; }  //collection navigation property
        //because one dept can have many employees, this is an one to many kind of relationship

    }
}
