using ConAppEFCode1.Models;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConAppEFCode1.Repositories
{
    public class DepartmentBO
    {
        OrganizationContext context;
        public DepartmentBO(OrganizationContext context)
        {
            this.context = context;
        }

        public bool AddDept(Department department)
        {
            bool b=false;
            DbSet<Department> departments=context.Departments; //calling the method departments we declared
            departments.Add(department);
            int r=context.SaveChanges();
            if (r > 0)
            {
                b = true;
            }
            return b;

        }

        public List<Department> GetDepartments()
        {
            DbSet<Department> deptList =context.Departments;
            return deptList.ToList();
        }


        public Department GetDepartmentById(int id)
        {
            DbSet<Department> departments = context.Departments;
            Department department=departments.Find(id);  //Find() to find only by primary key.. if find by name/loaction -- do it by Where extension method
            return department;
        }

        public bool RemoveDept(Department department) 
        {
            DbSet<Department> departments = context.Departments;
            departments.Remove(department);
            int r = context.SaveChanges();
            if (r > 0) 
            {
                return true;
            }
            else
            {
                return false;
            }
        
        }

        public bool ModifyDept(Department updateDept)
        {
            DbSet<Department> departments = context.Departments;
            Department department = departments.Find(updateDept.DeptId);
            department.DeptName = updateDept.DeptName;
            department.Location=updateDept.Location;
            int r=context.SaveChanges();
            if (r > 0)
            {
                return true;
            }
            return false;
        }

    }
}
