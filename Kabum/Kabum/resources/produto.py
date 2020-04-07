from flask_restful import Resource, reqparse
from models.produto import ProdutoModel


produtos =[
    {
        "brinde": 0,
        "oferta": 0,
        "oferta_inicio": 0,
        "nova_descricao": "index.html",
        "menus": [
            {
                "codigo": 1,
                "nome": "Hardware",
                "amigavel": "/hardware",
                "nome_url": "/Hardware"
            },
            {
                "codigo": 105,
                "nome": "SATA",
                "amigavel": "/hardware/ssd-2-5",
                "nome_url": "/Hardware/SATA"
            },
            {
                "codigo": 1231,
                "nome": "240.0 GB",
                "amigavel": "/hardware/ssd-2-5/240-0-gb",
                "nome_url": "/Hardware/SATA/240.0 GB"
            },
            {
                "codigo": 1432,
                "nome": "SSD",
                "amigavel": "/hardware/ssd-2-5/240-0-gb/ssd-2-5",
                "nome_url": "/Hardware/SATA/240.0 GB/SSD"
            }
        ],
        "menu": "Hardware/SATA/240.0 GB/SSD",
        "codigo": 85197,
        "nome": "SSD Kingston A400, 240GB, SATA, Leitura 500MB/s, Gravação 350MB/s - SA400S37/240G",
        "familia": {
            "codigo": 0,
            "nome": "Kingston",
            "titulo": "Fabricante",
            "produtos": [
                {
                    "codigo": 85198,
                    "nome": "SSD Kingston A400, 480GB, SATA, Leitura 500MB/s, Gravação 450MB/s - SA400S37/480G",
                    "preco": 635.18,
                    "preco_prime": 635.18,
                    "preco_antigo": 0,
                    "disponibilidade": 0,
                    "preco_desconto": 539.9,
                    "preco_desconto_prime": 539.9,
                    "link_descricao": "/produto/85198/ssd-kingston-a400-480gb-sata-leitura-500mb-s-grava-o-450mb-s-sa400s37-480g",
                    "foto": "https://images8.kabum.com.br/produtos/fotos/85198/85198_index_m.jpg",
                    "produto_prime": 0
                },
                {
                    "codigo": 85196,
                    "nome": "SSD Kingston A400, 120GB, SATA, Leitura 500MB/s, Gravação 320MB/s - SA400S37/120G",
                    "preco": 268.12,
                    "preco_prime": 268.12,
                    "preco_antigo": 0,
                    "disponibilidade": 0,
                    "preco_desconto": 227.9,
                    "preco_desconto_prime": 227.9,
                    "link_descricao": "/produto/85196/ssd-kingston-a400-120gb-sata-leitura-500mb-s-grava-o-320mb-s-sa400s37-120g",
                    "foto": "https://images6.kabum.com.br/produtos/fotos/85196/85196_index_m.jpg",
                    "produto_prime": 0
                },
                {
                    "codigo": 95217,
                    "nome": "SSD Kingston A400, 960GB, SATA, Leitura 500MB/s, Gravação 450MB/s - SA400S37/960G",
                    "preco": 1176.35,
                    "preco_prime": 1176.35,
                    "preco_antigo": 1246.94,
                    "disponibilidade": 0,
                    "preco_desconto": 999.9,
                    "preco_desconto_prime": 999.9,
                    "link_descricao": "/produto/95217/ssd-kingston-a400-960gb-sata-leitura-500mb-s-grava-o-450mb-s-sa400s37-960g",
                    "foto": "https://images7.kabum.com.br/produtos/fotos/95217/95217_1520016948_index_m.jpg",
                    "produto_prime": 0
                },
                {
                    "codigo": 107338,
                    "nome": "SSD Kingston KC600, 256GB, SATA, Leitura 550MB/s, Gravação 500MB/s - SKC600/256G",
                    "preco": 379.88,
                    "preco_prime": 379.88,
                    "preco_antigo": 510.47,
                    "disponibilidade": 0,
                    "preco_desconto": 322.9,
                    "preco_desconto_prime": 322.9,
                    "link_descricao": "/produto/107338/ssd-kingston-kc600-256gb-sata-leitura-550mb-s-grava-o-500mb-s-skc600-256g",
                    "foto": "https://images8.kabum.com.br/produtos/fotos/107338/ssd-kingston-kc600-256gb-sata-leitura-550mb-s-gravacao-500mb-s-skc600-256g_1572354349_m.jpg",
                    "produto_prime": 0
                },
                {
                    "codigo": 107339,
                    "nome": "SSD Kingston KC600, 512GB, SATA, Leitura 550MB/s, Gravação 520MB/s - SKC600/512G",
                    "preco": 642.24,
                    "preco_prime": 642.24,
                    "preco_antigo": 948.12,
                    "disponibilidade": 0,
                    "preco_desconto": 545.9,
                    "preco_desconto_prime": 545.9,
                    "link_descricao": "/produto/107339/ssd-kingston-kc600-512gb-sata-leitura-550mb-s-grava-o-520mb-s-skc600-512g",
                    "foto": "https://images9.kabum.com.br/produtos/fotos/107339/ssd-kingston-kc600-512gb-sata-leitura-550mb-s-gravacao-520mb-s-skc600-512g_1572360201_m.jpg",
                    "produto_prime": 0
                },
                {
                    "codigo": 107340,
                    "nome": "SSD Kingston KC600, 1024GB, SATA, Leitura 550MB/s, Gravação 520MB/s - SKC600/1024G",
                    "preco": 1211.65,
                    "preco_prime": 1211.65,
                    "preco_antigo": 1324.59,
                    "disponibilidade": 0,
                    "preco_desconto": 1029.9,
                    "preco_desconto_prime": 1029.9,
                    "link_descricao": "/produto/107340/ssd-kingston-kc600-1024gb-sata-leitura-550mb-s-grava-o-520mb-s-skc600-1024g",
                    "foto": "https://images0.kabum.com.br/produtos/fotos/107340/ssd-kingston-kc600-1024gb-sata-leitura-550mb-s-gravacao-520mb-s-skc600-1024g_ssd-kingston-kc600-1024gb-sata-leitura-550mb-s-gravacao-520mb-s-skc600-1024g_1572361632_m.jpg",
                    "produto_prime": 0
                },
                {
                    "codigo": 96984,
                    "nome": "SSD Kingston UV500, 960GB, SATA, Leitura 520MB/s, Gravação 500MB/s, Kit Upgrade - SUV500B/960G",
                    "preco": 2484.59,
                    "preco_prime": 2484.59,
                    "preco_antigo": 0,
                    "disponibilidade": 0,
                    "preco_desconto": 2111.9,
                    "preco_desconto_prime": 2111.9,
                    "link_descricao": "/produto/96984/ssd-kingston-uv500-960gb-sata-leitura-520mb-s-grava-o-500mb-s-kit-upgrade-suv500b-960g",
                    "foto": "https://images4.kabum.com.br/produtos/fotos/96984/96984_1528833317_m.jpg",
                    "produto_prime": 0
                },
                {
                    "codigo": 108159,
                    "nome": "SSD Kingston A400, 1920GB, SATA, Leitura 500MB/s, Gravação 450MB/s - SA400S37/1920G",
                    "preco": 1646.94,
                    "preco_prime": 1646.94,
                    "preco_antigo": 2078.7,
                    "disponibilidade": 0,
                    "preco_desconto": 1399.9,
                    "preco_desconto_prime": 1399.9,
                    "link_descricao": "/produto/108159/ssd-kingston-a400-1920gb-sata-leitura-500mb-s-grava-o-450mb-s-sa400s37-1920g",
                    "foto": "https://images9.kabum.com.br/produtos/fotos/108159/ssd-kingston-a400-1920gb-sata-leitura-500mb-s-gravacao-450mb-s-sa400s37-1920g_1579023050_m.jpg",
                    "produto_prime": 0
                }
            ],
        },
        "fotos": [
            "https://images7.kabum.com.br/produtos/fotos/85197/85197_index_g.jpg",
            "https://images7.kabum.com.br/produtos/fotos/85197/85197_1484306076_g.jpg",
            "https://images7.kabum.com.br/produtos/fotos/85197/85197_1484306080_g.jpg"
        ],
        "disponibilidade": 0,
        "fabricante": {
            "codigo": 50,
            "nome": "Kingston",
            "img": "https://images0.kabum.com.br/produtos/fabricantes/logo-kingston.jpg"
        },
        "preco": 394,
        "preco_prime": 394,
        "preco_desconto": 334.9,
        "preco_desconto_prime": 334.9,
        "preco_antigo": 0,
        "economize_prime": 0,
        "descricao": "Conheça o SSD A400 da Kingston. Performance incrível e tecnologia de ponta! Este SSD possui com a tecnologia 3D NAND (também chamada de V-NAND). Performance não será problema com este SSD. Ele possui uma controladora de última geração para velocidades de leitura e gravação de até 500MB/s e 350MB/s, este SSD é 10x mais rápido do que um HD tradicional para melhor desempenho, resposta ultrarrápida em multitarefas e um computador mais rápido de modo geral. O seu desktop merece esse grande upgrade de velocidade! Comparados a discos rígidos mecânicos, o SSD A400 aumenta de forma drástica a resposta do seu PC com tempos maravilhosos de inicialização, carregamento e transferência. Além dessa performance incrível, este SSD também é mais confiável e durável do que um disco rígido comum. Este A400 possui 240GB de capacidade, o tamanho certo para o que você precisa no dia a dia. Procurando SSD? Compre no KaBuM!",
        "tag_title": "",
        "tem_frete_gratis": 0,
        "frete_gratis_somente_prime": 0,
        "tag_description": "",
        "avaliacao_numero": 2033,
        "avaliacao_nota": 5,
        "desconto": 15,
        "is_openbox": 0,
        "produto_html": "<p><strong>Caracter&iacute;sticas:</strong></p><p>- Marca: Kingston</p><p>- Modelo: SA400S37/240G</p><p>&nbsp;</p><p><strong>Especifica&ccedil;&otilde;es:</strong></p><p>- Formato: 2,5 pol&nbsp;</p><p>- Interface: SATA Rev. 3.0 (6Gb/s) &mdash; compat&iacute;vel com a vers&atilde;o anterior SATA Rev. 2.0 (3Gb/s)</p><p>- Capacidades: 240GB</p><p>- NAND: TLC&nbsp;</p><p>- Performance de refer&ecirc;ncia - at&eacute; 500MB/s para leitura e 350MB/s para grava&ccedil;&atilde;o&nbsp;</p><p>- Temperatura de armazenamento: -40 &deg;C a 85 &deg;C&nbsp;</p><p>- Temperatura de opera&ccedil;&atilde;o: 0 &deg;C a 70 &deg;C</p><p>- Vibra&ccedil;&atilde;o quando em opera&ccedil;&atilde;o: 2,17G pico (7 &ndash; 800 Hz)</p><p>- Vibra&ccedil;&atilde;o quando n&atilde;o est&aacute; em opera&ccedil;&atilde;o: 20G pico (10 &ndash; 2000 Hz)</p><p>- Expectativa de vida &uacute;til: 1 milh&atilde;o de horas MTB</p><p>&nbsp;</p><p><strong>Benef&iacute;cios:&nbsp;</strong></p><p>- 10x mais r&aacute;pido do que um disco r&iacute;gido: Com incr&iacute;veis velocidades de leitura/grava&ccedil;&atilde;o, o SSD A400 n&atilde;o somente ir&aacute; aumentar o desempenho, como tamb&eacute;m poder&aacute; ser usado para dar vida nova em computadores mais antigos.&nbsp;</p><p>- Robusto: O A400 &eacute; resistente a impactos e vibra&ccedil;&otilde;es, para confiabilidade refor&ccedil;ada em notebooks e outros dispositivos m&oacute;veis.&nbsp;</p><p>- Ideal para desktops e notebooks: A400 tem um formato de 7 mm parase ajustar auma grande variedade de computadores. &Eacute; ideal para notebooks mais finos e computadores, ultrabooks e ultratop com espa&ccedil;o limitado.</p><p><strong><br /></strong></p><p><strong>Conte&uacute;do da embalagem:</strong></p><p>- SSD Kingston</p>",
        "dimensao_peso": 70,
        "peso": "70 gramas (bruto com embalagem)",
        "garantia": "1 ano de garantia",
        "codigo_anatel": "",
        "produto_especie": 0,
        "link_descricao": "/produto/85197/ssd-kingston-a400-240gb-sata-leitura-500mb-s-grava-o-350mb-s-sa400s37-240g",
        "origem": 0,
        "origem_nome": 0,
        "flag_blackfriday": 0,
        "sucesso": 0
    }
]


class Produtos(Resource):
    def get(self):
        return {'produtos': [produto.json() for produto in models.produto.ProdutoModel.query.all()]}


class Produto(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('preco', type =float, required=True, help= "The field 'preco' cannot be left blank")
    atributos.add_argument('preco_prime')
    atributos.add_argument('preco_desconto')
    atributos.add_argument('preco_desconto_prime')
    atributos.add_argument('preco_antigo', type =float, required=True, help= "The field 'preco antigo' cannot be left blank")



    def get(self, codigo):
        produto = models.produto.ProdutoModel.find_produto(codigo)
        if produto:
            return produto.json()

        return {'message': 'Produto not found'}, 404 # not found

    def post(self, codigo):
        if models.produto.ProdutoModel.find_produto(codigo):
            return {"message":"Codigo '{}' alredy existis." .format(codigo)}, 400 # Bad Request

        dados = Produto.argumentos.parse_args()
        produto = models.produto.ProdutoModel(codigo, **dados)
        try:
            produto.save_poduto()
        except:
            return {'messege': 'An internal error ocurred trying to save produto'}, 500 # An server error
        return produto.json()

    def put(self, codigo):

        dados = Produto.atributos.parse_args()
        produto_encontrado = models.produto.ProdutoModel.find_produto(codigo)
        if produto_encontrado:
            produto_encontrado.update_produto(**dados)
            produto_encontrado.save_produto()
            return produto_encontrado.json(), 200
        produto = models.produto.ProdutoModel(codigo, **dados)
        try:
            produto.save_poduto()
        except:
            return {'messege': 'An internal error ocurred trying to save produto'}, 500  # An server error
        return produto.json(), 201 #created

    def delete(self, codigo):

        produto = models.produto.ProdutoModel.find_produto(codigo)
        if produto:
            try:
                produto.delete_produto()
            except:
                return {'message': 'An error ocurred trying to delete produto'},500 # An server error
            return {'message': 'Produto Deleted.'}
        return {'messege': 'Produto not found.'}, 404