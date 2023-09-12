from services.VendaService import PedidoVendaService
import controllers.ConnectionDAO as db
from utils.common_functions import list_to_string

class PedidoVendaDAO(object):
    def __index__(self):
        pass

    def listar_pedido_bd(self, numero_pedido, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb'):
        con = db.conectar_db(servidor, local_bd)
        sql_ = """select PVDNUM, FUNCOD,CLICOD,TRNSEQ,TRNCXA,PVDTIPPRC,PVDDATEMI,PVDHOREMI,
        PVDDATFEC,PVDHORFEC,PVDSTATUS,
        PVDDOCIMP,PVDVLR,PVDDCN,PVDACR,PVDBLODCN,PVDBLOEST,PVDBLOLIMCRD,PVDFUNAUT,PVDCLIDES,PVDCLIEND,PVDCLIBAI,
        PVDCLICID,PVDCLIEST,PVDCLINUM,PVDCLICMP,PVDCLICEP,PVDCLICPFCGC,PVDCLITEL,PVDTIPEFET,OPECOD,CFOCOD,PVDTIPFRT,
        PVDDATPREV,PVDHORPREV,PVDTIPATD,PVDSTAPAF,PEDCODEXT,PVDLOCCOD,PVDCORCOD,PVDCLICODIBGE,PVDMOTDES,PVDOBS
        from pedido_venda
        where pvdnum = ?
        """
        cursor = con.cursor()
        cursor.execute(sql_, [numero_pedido.zfill(10)])
        #rs = cursor.fetchall()
        rs = cursor.fetchone()
        return rs

    def listar_itens_pedido_bd(self, numero_pedido, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb'):
        con = db.conectar_db(servidor, local_bd)
        sql = """select
        ID,PVISEQ,PVDNUM,pedido_venda_item.PROCOD,PVIQTD,PVIVLRUNI,PVIVLRDCN,PVITIPDCN,PVIVLRACR,PVITIPACR,PVISERPRO,
        PVIOBS,PVITRBID,PVIALQICMS,PVIITEEMB,PVIUNID,PVIPRODES,PVIPRODESDZ, produto.PROUNID,PVIPROCODAUX,PVIFUNCOD,
        PVIPRCPRAT,PVIQTDATD,PVITIP,PVIPRCVDA,PVI_CODIGO_GARANTIA,PVI_MESES_GARANTIA,
        PVI_PRECO_GARANTIA,PVI_PRECO_LIQ_GARANTIA,PVI_TIPO_GARANTIA,PVISTAPAF,PVIPRODESVAR,
        PVIDESVLR,PVINUMPEDCOMPCLI,PVIORDITEPEDCOMPCLI,PVIALQPIS,PVICSTPIS,PVIALQCOF,PVICSTCOF
        from pedido_venda_item
        left join produto on pedido_venda_item.procod = produto.procod
        where pvdnum = ?"""
        cursor = con.cursor()
        cursor.execute(sql, [numero_pedido.zfill(10)])
        rs = cursor.fetchall()
        return rs

    def atualizar_status_pedido_bd(self, numero_pedido, status_pedido,servidor='localhost',
                                   local_bd='c:/syspdv/syspdv_srv.fdb'):
        con = db.conectar_db(servidor, local_bd)
        sql = """update pedido_venda set pvdstatus = ?
              where pvdnum = ?
        """

        cursor = con.cursor()
        cursor.execute(sql, [status_pedido,numero_pedido])

    def listar_pre_finalizacao_pedido_bd(self, numero_pedido, servidor='localhost', local_bd='c:/syspdv/syspdv_srv.fdb'):
        con = db.conectar_db(servidor, local_bd)
        sql_ = """select pvdnum, fzdcod, prefzpvdvlr, prefzpvdtroco
        from prefnzpedidovenda
        where pvdnum = ?
        """
        cursor = con.cursor()
        cursor.execute(sql_, [numero_pedido.zfill(10)])
        #rs = cursor.fetchall()
        rs = cursor.fetchone()
        return rs

    def lista_pedido_api(self, url, access_token, inicio = 0, contador = 0):
        lista_pedidos = PedidoVendaService.get_pedidos(url, access_token, inicio, contador)
        if lista_pedidos is None:
            return None
        else:
            return lista_pedidos

    def lista_pedido_id_api(self, url, access_token, id_):
        resultado = PedidoVendaService.get_pedido_por_id(url, access_token, id_)
        if resultado is None:
            return None
        else:
            return resultado

    def lista_atendimento_pedido(self, url, access_token, id_):
        pass

    def salva_pedido_api(self, url, access_token, pedido_json):
        resultado = PedidoVendaService.post_add_pedido(url, access_token, pedido_json)
        #print('post pedido post_add_pedido:\n', pedido_json)
        if resultado is None:
            return None
        else:
            return resultado


