anti , b , c , d = map ( int , "4 0 0 4". split ( ) )
l = abs ( anti - c ) ; m = abs ( b - d )
if anti == c : print ( anti + m , b , c + m , d )
elif b == d : print ( anti , b + l , c , d + l )
elif l != m : print ( - 1 )
else : print ( anti , d , c , b )
