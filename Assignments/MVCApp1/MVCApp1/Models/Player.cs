using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;

namespace MVCApp1.Models
{
    enum Gender
    {
        Male,Female
    }
    public class Player
    {
        [DatabaseGenerated(DatabaseGeneratedOption.None)]
        public int PlayerId { get; set; }

        //[Required,MaxLength(30)]
        public string PlayerName { get; set; }

        //[Required, MaxLength(30)]
        public string Country { get; set; }

        [Required,Range(15,65)]
        public int Age { get; set; }

        [Required,EnumDataType(typeof(Gender))]
        public string Gender { get; set; }

        //[ForeignKey("Game")]
        public int GameId { get; set; }

        //reference navigation property for FK (one to many relationship)
        public Game Game { get; set; }
    }
}
