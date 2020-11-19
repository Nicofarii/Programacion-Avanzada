package deportista ;

public class Basqet implements Balones{

     @Override
    public void usar (){
        System.out.println("Usando balon de Basqet");
    }

    @Override
    public void usar (String conlamano){
        System.out.println("Usando balon de Basqet con la mano");
    }

    @Override
    public void usar (String conelpie){
        System.out.println("Usando balon de Basqet con el pie");
    }
}