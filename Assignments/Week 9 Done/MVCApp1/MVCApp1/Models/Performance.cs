using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace MVCApp1.Models
{
    public class Performance
    {
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int SerialId { get; set; }

        [ForeignKey("Player")]
        public int PlayerId { get; set; }

        [ForeignKey("GameEvent")]
        public int EventId { get; set; }

        [Required,MaxLength(200)]
        public string PerformanceRecord { get; set; }
        public int Rank { get; set; }

        //one to one relationship.. 
        //player and his performance are 1 to 1
        //therefore no ICollections which is used for many to one or vice versa

        public Player Player { get; set; }
        public GameEvent GameEvent { get; set; }


    }
}
