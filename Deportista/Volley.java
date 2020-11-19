package deportista;

public class Volley implements Balones{

    @Override
    public void usar (){
        System.out.println("Usando balon de Volley");
    }

    @Override
    public void usar (String conlamano){
        System.out.println("Usando balon de Volley con la mano");
    }

    @Override
    public void usar (String conelpie){
        System.out.println("Usando balon de Volley con el pie");
    }

}   