from services.ProdutoService import ProdutoService, CodigosAuxiliaresService, PrecoService
from services.ProdutoService import SecaoService, GrupoService, SubGrupoService
from services.ProdutoService import ProdutoFornecedorService
import controllers.ConnectionDAO as db
from utils.common_functions import list_to_string


class ProdutoDAO(object):
    def __init__(self):
        pass
    def lista_produtos_api(self, url, access_token, inicio = 0, contador = 0):
        lista_produtos = ProdutoService.get_produtos(url, access_token, inicio, contador)
        if lista_produtos is None:
            return None
        else:
            return lista_produtos

    def lista_produto_id_api(self, url, access_token, id_):
        resultado = ProdutoService.get_produto_id(url, access_token, id_)
        if resultado is None:
            return None
        else:
            return resultado

    def listar_produto_id_bd_local(self, procod, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb'):
        con = db.conectar_db(servidor, local_bd)
        sql_ = """select * from produto
            left join produto_forncedor on produto.procod = produto_fornecedor.procod  
            where produto.procod = ?          
        """
        cursor = con.cursor()
        cursor.execute(sql_, [procod])
        rs = cursor.fetchall()
        return rs

    def listar_produto_lista_filtro_bd_local(self, lista_codigos, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb'):
        con = db.conectar_db(servidor, local_bd)
        filtro = list_to_string(lista_codigos)
        sql_ = """
            select  produto.procod,procodint,procodorigem,prodes, prodesrdz,seccod,grpcod,sgrcod,trbid,
                    procest,natcodigo,proncm,proqtdetq,prodiaseg,prounid, provld, protaba,
                    pronumser,probontip,proctrest,procomp,proctrvld,proenvbal,promix,prodesvar,
                    proend, proforlin, proundcmp, proundref, procodanp, protipipi,proprcvar,
                    proiat,proippt, protipagr, profin, proinczf,properdcn,profrtloj,
                    proiteemb,procstmed,proqtdmaxvda,propesbrt,propesliq,promedref, proipi,provlragr,
                    properpda, prodcnmax,prodatcadinc,prodatcadalt,propesvar,gencodigo,procomtip,
                    procomcap,procompro,procomven,forcod,proestmin,proestmax,cmpqtd,cmpestven
                    from produto
                    left join composto on produto.procod=composto.procod                       
                    where produto.procod in ({})          
                    order by produto.procod
        """.format(filtro)
        cursor = con.cursor()
        cursor.execute(sql_)
        rs = cursor.fetchall()
        return rs

    def listar_produto_bd(self, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb', resumido=False):
        con = db.conectar_db(servidor, local_bd)
        if not resumido:
            sql = """select * from produto"""
        else:
            sql = """
                    select /*skip 90082*/ produto.procod,procodint,procodorigem,prodes, prodesrdz,seccod,grpcod,sgrcod,trbid,
                    procest,natcodigo,proncm,proqtdetq,prodiaseg,prounid, provld, protaba,
                    pronumser,probontip,proctrest,procomp,proctrvld,proenvbal,promix,prodesvar,
                    proend, proforlin, proundcmp, proundref, procodanp, protipipi,proprcvar,
                    proiat,proippt, protipagr, profin, proinczf,properdcn,profrtloj,
                    proiteemb,procstmed,proqtdmaxvda,propesbrt,propesliq,promedref, proipi,provlragr,
                    properpda, prodcnmax,prodatcadinc,prodatcadalt,propesvar,gencodigo,procomtip,
                    procomcap,procompro,procomven,forcod,proestmin,proestmax,cmpqtd,cmpestven
                    from produto
                    left join composto on produto.procod=composto.procod
                    where produto.procod>=1
                    and seccod in ('04','05')
                    --and prosincld='S'
                    /*and (prodatcadinc>='21.06.2022'
                     or prodatcadalt >='21.06.2022'
                     or proprcdatalt>='21.06.2022')*/
                    order by produto.procod                    
                """

        sql_cad_atualizado = """
                select /*skip 53063*/ produto.procod,procodint,procodorigem,prodes, prodesrdz,seccod,grpcod,sgrcod,trbid,
                procest,natcodigo,proncm,proqtdetq,prodiaseg,prounid, provld, protaba,
                pronumser,probontip,proctrest,procomp,proctrvld,proenvbal,promix,prodesvar,
                proend, proforlin, proundcmp, proundref, procodanp, protipipi,proprcvar,
                proiat,proippt, protipagr, profin, proinczf,properdcn,profrtloj,
                proiteemb,procstmed,proqtdmaxvda,propesbrt,propesliq,promedref, proipi,provlragr,
                properpda, prodcnmax,prodatcadinc,prodatcadalt,propesvar,gencodigo,procomtip,
                procomcap,procompro,procomven,forcod,proestmin,proestmax,cmpqtd,cmpestven
                from produto
                left join composto on produto.procod=composto.procod
                where prodatcadinc>='16.12.2020'
                order by produto.procod                    
            """
        cursor = con.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()
        return rs

    def listar_impostos_federais_produto(self, procod, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb'):
        con = db.conectar_db(servidor, local_bd)
        sql = "select * from impostos_federais_produto where procod = ? "
        cursor = con.cursor()
        cursor.execute(sql, [procod])
        rs = cursor.fetchall()
        codimpfed = []
        if rs is not None:
            for linha in rs:
                codimpfed.append(linha[0])
            return codimpfed
        else:
            return None

    def atualizar_status_cld(self, procod, status, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb'):
        con = db.conectar_db(servidor, local_bd)
        sql = "update produto set prosincld = ? where procod = ? "
        cursor = con.cursor()
        cursor.execute(sql, [status, procod])
        con.commit()


class CodigosAuxiliaresDAO(object):
    def __init__(self):
        pass

    def lista_auxiliares_api(self, url, access_token, inicio=0, contador=0):
        lista_produtos = CodigosAuxiliaresService.get_auxiliares(url, access_token, inicio, contador)
        if lista_produtos is None:
            return None
        else:
            return lista_produtos

    def lista_auxiliares_id_api(self, url, access_token, id_):
        resultado = CodigosAuxiliaresService.get_auxiliar_id(url, access_token, id_)
        if resultado is None:
            return None
        else:
            return resultado

    def salva_auxiliares_api(self, url, access_token, id_produto, auxiliar_json):
        resultado = CodigosAuxiliaresService.post_add_auxiliar(url, access_token, id_produto, auxiliar_json)
        if resultado is None:
            return None
        else:
            return resultado

    def listar_auxiliares_id_bd_local(self, procod, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb'):
        con = db.conectar_db(servidor, local_bd)
        sql = """
            select procodaux, procod, profatormult, proeantrib from produtoaux
            where procod = ? or procodaux = ?
        """
        cursor = con.cursor()
        cursor.execute(sql, [procod])
        rs = cursor.fetchall()
        return rs

    def listar_auxiliares_bd(self, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb'):
        con = db.conectar_db(servidor, local_bd)
        #quando apresentado erro, utilizo skip e número de códigos que deverá ser ignorado...Uma vez que a query é ordenada
        sql = """
            /*select skip 5008 procodaux, procod, profatormult, proeantrib from produtoaux*/
            /*where procod >= 3310 and procod<= 3320*/
            select px.procodaux, px.procod, px.profatormult, px.proeantrib 
            from produtoaux px
            left join produto p on p.procod = px.procod
            where p.prosincld='S'
            order by px.procod
        """
        sql_filtrado = """
        select procodaux, produtoaux.procod, profatormult, proeantrib from produtoaux
            inner join produto on produtoaux.procod = produto.procod
            /*where produto.prosincld='S'*/
            order by produtoaux.procod
        """
        cursor = con.cursor()
        #caso esteja reprocessando um conjunto menor, e filtrado por prosincld, utilizo sql_filtrado
        cursor.execute(sql)
        rs = cursor.fetchall()
        return rs

class PrecoDAO(object):
    def __init__(self):
        pass

    def lista_precos_api(self, url, access_token, inicio=0, contador=0):
        pass

    def pesquisa_id_tabela_preco_api(self, url, access_token, codigo_produto, id_loja):
        resultado = PrecoService.get_preco_id(url, access_token, codigo_produto, id_loja)
        return resultado

    def salva_precos_api(self, url, access_token, id_tabela,auxiliar_json):
        resultado = PrecoService.put_update_preco(url, access_token, id_tabela, auxiliar_json)
        if resultado is None:
            return None
        else:
            return resultado

    def listar_precos_pelo_id_api(self):
        pass

    def pesquisar_preco_codigo_bd(self, procod_informado, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb'):
        procod = str(procod_informado).zfill(14)
        con = db.conectar_db(servidor, local_bd)
        sql = """
            select procod, prodes, proprcvdavar, proprc1, proprcofevar, promrg1,
            proprcvda2, proprc2, proprcofe2, promrg2, proqtdminprc2,
            proprcvda3, proprc3, proprcofe3, promrg3, proqtdminprc3,
            prodcnmax, properdcn from produto 
            where proforlin<>'S' and procod = ?
            order by procod       
        """

        cursor = con.cursor()
        cursor.execute(sql, [procod])
        rs = cursor.fetchall()
#        for linha in rs:
#            print(linha)
        return rs[0]

    def listar_precos_bd(self, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb'):
        con = db.conectar_db(servidor, local_bd)
        sql = """            
            select /*SKIP 69865*/ procod, prodes, proprcvdavar, proprc1, proprcofevar, promrg1,
            proprcvda2, proprc2, proprcofe2, promrg2, proqtdminprc2,
            proprcvda3, proprc3, proprcofe3, promrg3, proqtdminprc3,
            prodcnmax, properdcn from produto
            where proforlin<>'S'
            and proprcvdavar<>0
            and prosincld='S'
            order by procod       
        """

        sql_datado = """select /*SKIP 8587*/ procod, prodes, proprcvdavar, proprc1, proprcofevar, promrg1,
            proprcvda2, proprc2, proprcofe2, promrg2, proqtdminprc2,
            proprcvda3, proprc3, proprcofe3, promrg3, proqtdminprc3,
            prodcnmax, properdcn from produto
                where  proprcvdavar<>0
                AND (prodatcadalt>='21.06.2022'
                or prodatcadinc>='21.06.2022'
                or proprcdatalt>='21.06.2022')
            order by prodatcadinc desc
        """

        sql_uso_loja_nova = """            
            select /*SKIP 5606*/ procod, prodes, proprcvdavar, proprc1, proprcofevar, promrg1,
            proprcvda2, proprc2, proprcofe2, promrg2, proqtdminprc2,
            proprcvda3, proprc3, proprcofe3, promrg3, proqtdminprc3,
            prodcnmax, properdcn from produto
            where proforlin<>'S'
            and proprcvdavar>0
            and procod>100000
            /*and prosincld='S'*/
            order by procod       
        """

        cursor = con.cursor()
        cursor.execute(sql)
        #cursor.execute(sql_datado)
        rs = cursor.fetchall()
        return rs

class SecaoDAO(object):
    def __init__(self):
        pass

    def lista_secao_api(self, url, access_token, inicio=0, contador=0):
        lista_secoes = SecaoService.get_secoes(url, access_token, inicio, contador)
        if lista_secoes is None:
            return None
        else:
            return lista_secoes

    def lista_secao_id_api(self, url, access_token, id_):
        resultado = SecaoService.get_secao_id(url, access_token, id_)
        if resultado is None:
            return None
        else:
            return resultado

    def salva_secao_api(self, url, access_token, auxiliar_json):
        resultado = SecaoService.post_add_secao(url, access_token, auxiliar_json)
        if resultado is None:
            return None
        else:
            return resultado

    def listar_secao_id_bd_local(self, seccod, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb'):
        con = db.conectar_db(servidor, local_bd)
        sql = """
            select seccod, secdes from secao
            where seccod = ?
        """
        cursor = con.cursor()
        cursor.execute(sql, [seccod])
        rs = cursor.fetchall()
        return rs

    def listar_secao_bd(self, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb', resumido=False):
        con = db.conectar_db(servidor, local_bd)
        sql = """
            select seccod, secdes from secao order by seccod
        """
        cursor = con.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()
        return rs

class GrupoDAO(object):
    def __init__(self):
        pass

    def lista_grupo_api(self, url, access_token, id_secao, inicio=0, contador=0):
        lista_grupos = GrupoService.get_grupos(url, access_token, id_secao,inicio, contador)
        if lista_grupos is None:
            return None
        else:
            return lista_grupos


    def salva_grupo_api(self, url, access_token, id_secao, auxiliar_json):
        resultado = GrupoService.post_add_grupo(url, access_token, id_secao, auxiliar_json)
        if resultado is None:
            return None
        else:
            return resultado

    def listar_grupo_id_bd_local(self, seccod, grpcod, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb'):
        con = db.conectar_db(servidor, local_bd)
        sql = """
            select seccod, grpcod, grpdes from grupo
            where seccod = ? and grpcod = ?
        """
        cursor = con.cursor()
        cursor.execute(sql, [seccod, grpcod])
        rs = cursor.fetchall()
        return rs

    def listar_grupos_bd(self, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb', resumido=False):
        con = db.conectar_db(servidor, local_bd)
        sql = """
            select seccod, grpcod, coalesce(grpdes, 'EM_BRANCO') from grupo 
            where grpcod<>'000'
            order by seccod, grpcod
        """
        cursor = con.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()
        return rs

class SubGrupoDAO(object):
    def __init__(self):
        pass

    def lista_subgrupo_api(self, url, access_token, id_secao, id_grupo, inicio=0, contador=0):
        lista_subgrupos = SubGrupoService.get_subgrupos(url, access_token, id_secao, id_grupo, inicio, contador)
        if lista_subgrupos is None:
            return None
        else:
            return lista_subgrupos


    def salva_subgrupo_api(self, url, access_token, id_secao, id_grupo, auxiliar_json):
        resultado = SubGrupoService.post_add_subgrupo(url, access_token, id_secao, id_grupo, auxiliar_json)
        if resultado is None:
            return None
        else:
            return resultado

    def listar_subgrupo_id_bd_local(self, seccod, grpcod, sgrcod, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb'):
        con = db.conectar_db(servidor, local_bd)
        sql = """
            select seccod, grpcod, sgrcod, coalesce(sgrdes, 'EM_BRANCO') from subgrupo
            where seccod = ? and grpcod = ? and sgrcod = ?
        """
        cursor = con.cursor()
        cursor.execute(sql, [seccod, grpcod, sgrcod])
        rs = cursor.fetchall()
        return rs

    def listar_subgrupos_bd(self, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb', resumido=False):
        con = db.conectar_db(servidor, local_bd)
        sql = """
            select seccod, grpcod, sgrcod, coalesce(sgrdes, 'EM_BRANCO') 
            from subgrupo 
            where grpcod<>'000' and sgrcod<>'000'
            order by seccod, grpcod, sgrcod
        """
        cursor = con.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()
        return rs

class ProdutoFornecedorDAO(object):
    def __init__(self):
        pass

    def lista_produto_fornecedor_api(self, url, access_token, id_produto):
        lista_referencias = ProdutoFornecedorService.get_produto_fornecedor(url, access_token, id_produto)
        if lista_referencias is None:
            return None
        else:
            return lista_referencias

    def salva_produto_fornecedor_api(self, url, access_token, id_produto, produto_json):
        resultado = ProdutoFornecedorService.post_add_produto_fornecedor(url, access_token, id_produto, produto_json)
        if resultado is None:
            return None
        else:
            return resultado

    def lista_produto_fornecedor_bd(self, servidor, local_bd):
        con = db.conectar_db(servidor, local_bd)
        sql = """
            select produto_fornecedor.procod, produto_fornecedor.forcod,
            prfreffor, prfunid, prfqtd, prfnivel 
            from produto_fornecedor 
            left join produto on produto_fornecedor.procod = produto.procod
            where 1=1
            and prosincld = 'S'
            and procod>='07896111921722'
            order by procod
        """

        sql_datado = """
        select produto_fornecedor.procod, produto_fornecedor.forcod, prfreffor, prfunid, prfqtd, prfnivel from 
            produto_fornecedor 
            left join produto on produto_fornecedor.procod = produto.procod
            where prodatcadalt>='30.06.2020'
                or prodatcadinc>='30.06.2020'
                or proprcdatalt>='30.06.2020'
            order by produto_fornecedor.procod                           
        """
        cursor = con.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()
        return rs


