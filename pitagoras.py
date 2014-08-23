#-*- coding: utf-8 -*-
import math;

def programa():
    print
    print "Programa que calcula la hipotenusa:"
    print "ingrese los lados de un triangulo rectangulo" 
    print "(si no ingresas nada por defecto sera 1 unidad)"
    print
    
    b=(raw_input("ingrese lado b: "));
    c=(raw_input("ingrese lado c: "));
    
    if b=="":
            b=1.0;
    if c=="":
            c=1.0;
            
    b2=math.pow((float)(b),2);
    c2=math.pow((float)(c),2);
    br=math.sqrt(b2);
    cr=math.sqrt(c2);
    print
    print "/////////////////resultado.////////////////////"
    print
    print "a^2 = b^2 + c^2"
    print
    print "a","^2 =",b,"^2 +",c,"^2"
    print
    print "a^2", "=", b2 , "+", c2
    print 
    print "a","= raiz de(",b2,"+",c2,")"
    print
    print "a", "=", br, "+", cr
    print
    print "a =",br+cr
    print "///////////////////////////////////////////////////"
    print
    
    r=(raw_input("Quiere volver a correr el programa? (S/n)"))
    if r=="S" or r=="SI" or r=="s" or r=="si": 
        programa();
    
programa();


