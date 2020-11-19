package deportista;

public class Jugador extends Persona{

    public void jugar(Balones b, String uso){

        b.usar(uso);
        b.inflar();
        

    }


}