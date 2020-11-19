package deportista;

public class Futbol implements Balones{

     @Override
    public void usar (){
        System.out.println("Usando balon de Futbol");
    }

    @Override
    public void usar (String conlamano){
        System.out.println("Usando balon de Futbol con la mano");
    }

    @Override
    public void usar (String conelpie){
        System.out.println("Usando balon de Futbol con el pie");
    }
}