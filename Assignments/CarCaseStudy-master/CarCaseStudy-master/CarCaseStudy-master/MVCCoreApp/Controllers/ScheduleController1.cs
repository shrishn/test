using Microsoft.AspNetCore.Mvc;
using MVCCoreApp.Models;
using System.Linq;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Mvc.Rendering;
using System.Security.Policy;

namespace MVCCoreApp.Controllers
{
    public class ScheduleController : Controller
    {
        private readonly JourneyDbContext _context;

        public ScheduleController(JourneyDbContext context)
        {
            _context = context;
        }

        // **GET: Schedule/Index (Display all schedules)**
        public IActionResult Index()
        {
            var schedules = _context.Schedules
                                     .Include(s => s.Car)
                                     .Include(s => s.Driver)
                                     .ToList();
            return View(schedules);
        }


        [HttpGet]
        public IActionResult AddSchedule()
        {
            ViewBag.Cars = new SelectList(_context.Cars, "CarId", "CarModel");
            ViewBag.Drivers = new SelectList(_context.Drivers, "DriverId", "DriverName");
            return View();
        }
        [HttpPost]
        public IActionResult AddSchedule(Schedules model)
        {
            if (ModelState.IsValid)
            {
                try
                {
                    _context.Schedules.Add(model);  // Only add IDs and primitive fields
                    _context.SaveChanges();  // Save to the database
                    TempData["SuccessMessage"] = "Schedule added successfully!";
                    return RedirectToAction("Index");
                }
                catch (Exception ex)
                {
                    TempData["ErrorMessage"] = $"Error: {ex.Message}";
                    return View(model);
                }
            }

            // If invalid, re-populate the ViewBag for dropdowns
            ViewBag.Cars = new SelectList(_context.Cars, "CarId", "CarModel");
            ViewBag.Drivers = new SelectList(_context.Drivers, "DriverId", "DriverName");
            TempData["ErrorMessage"] = "Please fill all required fields.";
            return View(model);
        }


        // GET: Edit Schedule
        [HttpGet]
        public IActionResult EditSchedule(int id)
        {
            var schedule = _context.Schedules.Find(id);
            if (schedule == null)
            {
                return NotFound();
            }

            // Populate dropdowns
            ViewBag.Cars = new SelectList(_context.Cars.ToList(), "CarId", "CarModel");
            ViewBag.Drivers = new SelectList(_context.Drivers.ToList(), "DriverId", "DriverName");
            return View(schedule);
        }

        // POST: Edit Schedule
        [HttpPost]
        public IActionResult EditSchedule(Schedules model)
        {
            if (!ModelState.IsValid)
            {
                // Populate dropdowns in case of validation failure
                ViewBag.Cars = new SelectList(_context.Cars.ToList(), "CarId", "CarModel");
                ViewBag.Drivers = new SelectList(_context.Drivers.ToList(), "DriverId", "DriverName");
                return View(model);
            }

            var scheduleToUpdate = _context.Schedules.Find(model.ScheduleId);
            if (scheduleToUpdate != null)
            {
                scheduleToUpdate.JourneyDate = model.JourneyDate;
                scheduleToUpdate.CarId = model.CarId;
                scheduleToUpdate.DriverId = model.DriverId;
                scheduleToUpdate.StartLocation = model.StartLocation;
                scheduleToUpdate.Destination = model.Destination;
                scheduleToUpdate.TotalKmDriven = model.TotalKmDriven;
                scheduleToUpdate.RatePerKm = model.RatePerKm;

                _context.Schedules.Update(scheduleToUpdate);
                _context.SaveChanges();
                TempData["SuccessMessage"] = "Schedule updated successfully!";
                return RedirectToAction("Index");
            }

            return NotFound();
        }

        // GET: Delete Schedule
        [HttpGet]
        public IActionResult DeleteSchedule(int id)
        {
            var schedule = _context.Schedules.Find(id);
            if (schedule == null)
            {
                return NotFound();
            }

            return View(schedule);
        }

        // POST: Delete Schedule
        [HttpPost, ActionName("DeleteSchedule")]
        public IActionResult ConfirmDeleteSchedule(int id)
        {
            var scheduleToDelete = _context.Schedules.Find(id);
            if (scheduleToDelete != null)
            {
                _context.Schedules.Remove(scheduleToDelete);
                _context.SaveChanges();
                TempData["SuccessMessage"] = "Schedule deleted successfully!";
                return RedirectToAction("Index");
            }

            return NotFound();
        }

    }
}
