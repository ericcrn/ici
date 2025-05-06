typedef struct Nodo {
    int num;
    char letra;
    struct Nodo *siguiente;
} *TipoPila;


extern TipoPila crearPila();
extern TipoPila insertarTope(TipoPila lista, int num, char letra);
extern TipoPila borrarTope(TipoPila lista);
extern TipoPila borrarPila(TipoPila lista);
extern int esPilaVacia(TipoPila p);
extern TipoPila verTopePila(TipoPila lista);