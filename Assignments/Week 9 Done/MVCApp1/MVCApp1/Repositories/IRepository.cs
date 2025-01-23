namespace MVCApp1.Repositories
{
    public interface IRepository<T> where T : class
    {
        bool Add(T entity);
        bool Remove(T entity);
        bool Modify (T entity);
        List<T> GetAllDetails();

        T Search(object Id);


    }
}
