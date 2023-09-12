from services.PessoaService import ClienteService, FornecedorService, FuncionarioService
import controllers.ConnectionDAO as db


class ClienteDAO(object):
    def __int__(self):
        pass

    def lista_clientes_ws(self, url, access_token, inicio = 0, contador = 0):
        lista_produtos = ClienteService.get_clientes(url, access_token, inicio, contador)
        if lista_produtos is None:
            return None
        else:
            return lista_produtos


    def lista_cliente_id_ws(self, url, access_token, id_):
        resultado = ClienteService.get_cliente_id(url, access_token, id_)
        if resultado is None:
            return None
        else:
            return resultado

    def lista_cliente_bd(self, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb', resumido=False):
        con = db.conectar_db(servidor, local_bd)
        if resumido == False:
            sql = """select * from cliente"""
        else:
            sql = """
                    select clicod, clides, cliend, clicpfcgc, clibai, clitel, clicep, clicid, clinum, clicmp,
                    cliest,clifan, clirgcgf, clipfpj, clitel2, cliemail,clisex,clipntref,clisitobs, clipais,
                    clicodigoibge
                    from cliente where clicod>='000000000000001'
                    /*and clisincld='S'*/
                    order by clicod
                """
        cursor = con.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()
        print(rs)
        return rs


    def lista_cliente_id_bd(self, id_):
        pass


    def salva_cliente_api(self, url, access_token, cliente_json):
        resultado = ClienteService.post_add_cliente(url, access_token, cliente_json)
        #print('cliente_json_metodo salva_cliente_api:\n', cliente_json)
        if resultado is None:
            return None
        else:
            return resultado


class FornecedorDAO(object):
    def __init__(self):
        pass

    def lista_fornecedores_ws(self, url, access_token, inicio = 0, contador = 0):
        lista_fornecedores = FornecedorService.get_fornecedores(url, access_token, inicio, contador)
        if lista_fornecedores is None:
            return None
        else:
            return lista_fornecedores


    def lista_fornecedor_id_ws(self, url, access_token, id_):
        resultado = FornecedorService.get_fornecedor_id(url, access_token, id_)
        if resultado is None:
            return None
        else:
            return resultado

    def lista_fornecedor_bd(self, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb', resumido=False):
        con = db.conectar_db(servidor, local_bd)
        if resumido == False:
            sql = """select * from fornecedor"""
        else:
            sql = """
                    select
                    forcod, forcon, forobs, fortabprz, forprz,forprzent,fortrans,forcgf,forcgc,
                    fordes, forfan, fortel, forfax, foremail, forsuf, forpfpj, forcep,
                    forest, forcodibge, forcid, forend, fornum, forbai, forcmp,forpais, forprodrur
                    from fornecedor
                    where 1=1 
                    and FORCOD>='000000000000001'
                    and forsincld='S'
                    order by forcod
                """
        cursor = con.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()
        return rs


    def lista_fornecedor_id_bd(self, id_):
        pass


    def salva_fornecedor_api(self, url, access_token, fornecedor_json):
        resultado = FornecedorService.post_add_fornecedor(url, access_token, fornecedor_json)
        if resultado is None:
            return None
        else:
            return resultado


class FuncionarioDAO(object):
    def __init__(self):
        pass

    def lista_funcionarios_ws(self, url, access_token, inicio = 0, contador = 0):
        lista_funcionarios = FuncionarioService.get_funcionarios(url, access_token, inicio, contador)
        if lista_funcionarios is None:
            return None
        else:
            return lista_funcionarios


    def lista_funcionario_id_ws(self, url, access_token, id_):
        resultado = FuncionarioService.get_funcionario_id(url, access_token, id_)
        if resultado is None:
            return None
        else:
            return resultado

    def lista_funcionario_bd(self, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb', resumido=False):
        con = db.conectar_db(servidor, local_bd)
        if resumido == False:
            sql = """select * from funcionario"""
        else:
            sql = """
                select
                FUNCOD,FUNDES,FUNAPE,FUNACE,FUNCAR,FUNCOM,FUNCOM2,FUNCOM3,FUNTPRC,FUNEMAIL,FUNLIMDCN,FUNINATIVO,
                FUNCOMMT,FUNCPF,FUNSINCLD,FUNEXBALEACD,FUNEXBALESPD,FUNEXBALEAUL,FUNEXBALEAPP
                    from funcionario                    
                    order by FUNCOD
                """
        cursor = con.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()
        return rs


    def lista_funcionario_id_bd(self, id_):
        pass


    def salva_funcionario_api(self, url, access_token, funcionario_json):
        resultado = FuncionarioService.post_add_funcionario(url, access_token, funcionario_json)
        if resultado is None:
            return None
        else:
            return resultado


