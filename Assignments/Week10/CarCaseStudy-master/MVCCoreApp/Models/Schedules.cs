using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;
using Microsoft.AspNetCore.Mvc.ModelBinding.Validation;
using MVCCoreApp.Models;

namespace MVCCoreApp.Models
{
    public class Schedules
    {
        [Key, DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int ScheduleId { get; set; }

        [Required(ErrorMessage = "Journey Date must not be left empty")]
        [DataType(DataType.Date), DisplayFormat(DataFormatString = "{0:dd-MM-yyyy}")]
        public DateTime JourneyDate { get; set; }

        [Required(ErrorMessage = "Please select a Car")]
        public string CarId { get; set; }

        [Required(ErrorMessage = "Please select a Driver")]
        public int DriverId { get; set; }

        public string StartLocation { get; set; }
        public string Destination { get; set; }

        [Required(ErrorMessage = "Total KM Driven must be specified")]
        public decimal TotalKmDriven { get; set; }

        [Required(ErrorMessage = "Rate per KM must be specified")]
        public int RatePerKm { get; set; }
        [ValidateNever]
        public virtual Car Car { get; set; }
        [ValidateNever]
        public virtual Driver Driver { get; set; }
    }
}

