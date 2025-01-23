using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;

namespace MVCApp1.Models
{
    public class GameEvent
    {
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }
        [Required, MaxLength(30)]
        public string TournamentName { get; set; }
        [Required, MaxLength(30)]
        public string EventName { get; set; }
        [Required, MaxLength(30)]
        public string Venue { get; set; }
        [Required]
        public DateTime EventDate { get; }

        public ICollection<Performance> Performances { get; set; }
        //ICollection for the property which is used for many type of relationship
    }
}
