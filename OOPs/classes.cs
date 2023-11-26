public class measurement{
    int height;
    int weight;
    int waist;

    public int bmi(){
        return weight/(height**2);
    }
}
measurement ratnesh= new measurement();
Console.Write(ratnesh.bmi(100,1.84));