class Casilla:
    def __init__(self, nave=None):
        self.nave = nave
        self.disparada = False

        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2

    def disparar(self):
        print("Estoy comprobando el impacto")

        # Si ya se había disparado antes
        if self.disparada:
            print("Ya se había disparado aquí")

            if self.nave is None:
                return self.AGUA
            elif self.nave.hundido:
                return self.HUNDIDO
            else:
                return self.TOCADO

        # Marcamos como disparada
        self.disparada = True

        # Si no hay nave
        if self.nave is None:
            return self.AGUA

        # Si hay nave
        else:
            return self.nave.recibir_disparo()