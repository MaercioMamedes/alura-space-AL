from django.contrib.auth.models import User


class Validation:

    @classmethod
    def field_is_alphanumeric(cls, obj_clean, field, field_name):
        if field is not None:

            for digit in field:
                if digit.isdigit():
                 obj_clean.add_error(field_name,'Não pode ser numérico')
                 break
               
                
    
    @classmethod
    def username_exist(cls, obj_clean, username):
        if User.objects.filter(username=username).exists():
           obj_clean.add_error('username',"Este usuário já foi cadastrado")
           
        
    
    @classmethod
    def password_validate(clas, obj_clean, password, password_confirm):

        if ' ' in password:
            obj_clean.add_error('password', 'A senha cadastrada não pode ser espaço vazio')
        
        if password != password_confirm:
            obj_clean.add_error('password_confirm', 'As senhas digitadas devem ser iguais')