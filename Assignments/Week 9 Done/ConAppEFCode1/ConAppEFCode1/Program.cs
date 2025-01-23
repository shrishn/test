using ConAppEFCode1.Models;
using ConAppEFCode1.Repositories;

namespace ConAppEFCode1
{
    public class Program
    {
        public static void Main(string[] args)
        {
            DepartmentBO dbo = new DepartmentBO(new Models.OrganizationContext());
            bool ans = true;

            Console.WriteLine("Add new record? Press Y");
            ans = Console.ReadLine().ToUpper()[0] == 'Y' ? true : false;
            while (ans)
            {
                Console.WriteLine("Enter Department Name and Location");
                string deptName = Console.ReadLine();
                string location = Console.ReadLine();
                Department dept = new Department()
                {
                    DeptName = deptName,
                    Location = location
                };
                bool b = dbo.AddDept(dept);
                if (b)
                {
                    Console.WriteLine("Department record created !");
                }

                Console.WriteLine("Create another record? Press Y");
                ans = Console.ReadLine().ToUpper()[0] == 'Y' ? true : false;
            }

            Console.WriteLine("Departments are ....");

            List<Department> deptList = dbo.GetDepartments();
            foreach (Department dept in deptList)
            {
                Console.WriteLine($"{dept.DeptId,5}{dept.DeptName,30}{dept.Location,30}");
            }

            Console.WriteLine("Want to edit record? Press Y");
            ans = Console.ReadLine().ToUpper()[0] == 'Y' ? true : false;
            while (ans)
            {
                Console.WriteLine("Enter Department Id");
                int deptId4 = Convert.ToInt32(Console.ReadLine());
                Department dept4 = dbo.GetDepartmentById(deptId4);
                Console.WriteLine("Enter Department Name and Location");
                dept4.DeptName = Console.ReadLine();
                dept4.Location = Console.ReadLine();

                bool b = dbo.ModifyDept(dept4);
                if (b)
                {
                    Console.WriteLine("Department Modified");
                }

                Console.WriteLine("Create another record? Press Y");
                ans = Console.ReadLine().ToUpper()[0] == 'Y' ? true : false;
            }

            Console.WriteLine("Search record? Press Y");
            ans = Console.ReadLine().ToUpper()[0] == 'Y' ? true : false;
            while (ans)
            {
                Console.WriteLine("Enter Department Id");
                int deptId = Convert.ToInt32(Console.ReadLine());

                Department dept2 = dbo.GetDepartmentById(deptId);
                if (dept2 != null)
                {
                    Console.WriteLine($"{dept2.DeptId,5}{dept2.DeptName,30}{dept2.Location,30}");
                }
                else
                {
                    Console.WriteLine("Department is not available");
                }
                Console.WriteLine("Search another record? Press Y");
                ans = Console.ReadLine().ToUpper()[0] == 'Y' ? true : false;
            }

            Console.WriteLine("Delete a record? Press Y");
            ans = Console.ReadLine().ToUpper()[0] == 'Y' ? true : false;
            while (ans)
            {

                Console.WriteLine("Enter Department Id for remove...");
                int deptId2 = Convert.ToInt32(Console.ReadLine());
                Department dept3 = dbo.GetDepartmentById(deptId2);

                if (dbo.RemoveDept(dept3))
                {
                    Console.WriteLine("Department Deleted");
                }
                Console.WriteLine("Delete another record? Press Y");
                ans = Console.ReadLine().ToUpper()[0] == 'Y' ? true : false;
            }

            Console.WriteLine("Re-run Application? Press Y");
            ans = Console.ReadLine().ToUpper()[0] == 'Y' ? true : false;
            if (ans)
            {
                Main(args);
            }
        }
    }
}

//public static void Main(string[] args)
//{
//   DepartmentBO dbo = new DepartmentBO(new Models.OrganizationContext());
//   bool ans=true;
//    while (ans)
//    {
//        Console.WriteLine("Enter department Name and Location");
//        string deptName=Console.ReadLine();
//        string location=Console.ReadLine();
//        Department dept=new Department()
//        {
//            DeptName=deptName,
//            Location=location
//        };

//        bool b=dbo.AddDept(dept);
//        if (b)
//        {
//            Console.WriteLine("Department record created");
//        }
//        Console.WriteLine("Create another record? Press Y");
//        ans = (Console.ReadLine().ToUpper()[0]=='Y' ?true :false);


//        Console.WriteLine("Departments are.....");
//        List<Department> deptList = dbo.GetDepartments();
//        foreach (Department department in deptList)
//        {
//            Console.WriteLine($"{dept.DeptId,5} {dept.DeptName,30} {dept.Location}");
//        }

//        Console.WriteLine("Enter the Department Id");
//        int deptId=Convert.ToInt32(Console.ReadLine());

//        Department dept2=dbo.GetDepartmentById(deptId);
//        if (dept2 != null) 
//        {
//            Console.WriteLine($"{dept.DeptId,5} {dept.DeptName,30} {dept.Location}");
//        }
//        else
//        {
//            Console.WriteLine("Department is not available");
//        }

//        Console.WriteLine("Enter the Department Id to remove...");
//        int deptId3=Convert.ToInt32(Console.ReadLine());
//        Department dept3=dbo.GetDepartmentById(deptId);
//        if (dbo.RemoveDept(dept3))
//        {
//            Console.WriteLine("Record removed");
//        }
//        else
//        {
//            Console.WriteLine("Entered dept id id invalid");
//        }
//    }

//}