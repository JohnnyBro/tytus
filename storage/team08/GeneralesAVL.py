import pickle

class Generales:

    #rotaciones
    def srl(self, t1):
        t2 = t1.izquierda
        t1.izquierda = t2.derecha
        t2.derecha = t1
        t1.nivel = self.maxi(self.nivel(t1.izquierda), self.nivel(t1.derecha))+1
        t2.nivel = self.maxi(self.nivel(t2.izquierda), t1.nivel)+1
        return t2

    def srr(self, t1):
        t2 = t1.derecha
        t1.derecha = t2.izquierda
        t2.izquierda = t1
        t1.nivel = self.maxi(self.nivel(t1.izquierda), self.nivel(t1.derecha))+1
        t2.nivel = self.maxi(self.nivel(t2.izquierda), t1.nivel)+1
        return t2

    def drl(self, tmp):
        tmp.izquierda = self.srr(tmp.izquierda)
        return self.srl(tmp)

    def drr(self, tmp):
        tmp.derecha = self.srl(tmp.derecha)
        return self.srr(tmp)

    def jalarValN(self, vali):
        return sum(ord(x) for x in vali)

    def nivel(self, tmp):
        if tmp is None:
            return -1
        else:
            return tmp.nivel
        
    def maxi(self, r, l):
        return (l,r)[r>l]

    def Balance(self, tmp):
        if not tmp:
            return 0
        return self.Balance(tmp.izquierda) - self.nivel(tmp.derecha)
    
    def leMenor(self, tmp):
        if tmp is None or tmp.izquierda is None:
            return tmp
        return self.leMenor(tmp.izquierda)

    def commitBase(self, contenido):
        with open('Base.bin', 'wb') as f:
            datos = contenido
            pickle.dump(datos, f )
        
    
    def loadBase(self):
        with open('Base.bin', 'rb') as g:
            datos = pickle.load(g)
            return datos
        
    def commitTabla(self, contenido):
        with open('Tabla.bin', 'wb') as f:
            datos = contenido
            pickle.dump(datos, f )
        
    
    def loadTabla(self):
        with open('Tabla.bin', 'rb') as g:
            datos = pickle.load(g)
            return datos
    

g = Generales()