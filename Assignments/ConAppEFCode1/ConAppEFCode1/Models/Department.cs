using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConAppEFCode1.Models
{
    [Table("Department")]
    public class Department
    {
        [Key,DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int DeptId { get; set; }
        [Required , MaxLength(30)] 
        public string DeptName { get; set; }
        [Required, MaxLength(30)]
        public string Location { get; set; }
    }
}
