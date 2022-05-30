INSERT INTO blog_corretora(id,	nome, usuario, senha, aplicativo, server, empresa, ambiente, moeda, saldo, "capitalLig", "roboEnvioOrdem", "roboRecebimentoOrdem", "roboUpdateOrdem",created,updated)
	VALUES (1,'NOME', 54901332, 'N6j7y7a5', 'METATARDER 5', 'server', 'empresa', 'D', 'BRL', 0.0,0.0,'','','','2020-01-01','2020-01-01'),
		   (2,'NOME', 64901332, 'N6j7y7a5', 'METATARDER 5', 'server', 'empresa', 'D', 'BRL', 0.0,0.0,'','','','2020-01-01','2020-01-01'),
		   (3,'NOME', 74901332, 'N6j7y7a5', 'METATARDER 5', 'server', 'empresa', 'D', 'BRL', 0.0,0.0,'','','','2020-01-01','2020-01-01'),
		   (4,'NOME', 84901332, 'N6j7y7a5', 'METATARDER 5', 'server', 'empresa', 'D', 'BRL', 0.0,0.0,'','','','2020-01-01','2020-01-01'),
		   (5,'NOME', 94901332, 'N6j7y7a5', 'METATARDER 5', 'server', 'empresa', 'D', 'BRL', 0.0,0.0,'','','','2020-01-01','2020-01-01'),
           (6,'NOME', 54951867, 'N6j7y7a5', 'METATARDER 5', 'server', 'empresa', 'D', 'BRL', 0.0,0.0,'','','','2020-01-01','2020-01-01'),
		   (7,'NOME', 64951867, 'N6j7y7a5', 'METATARDER 5', 'server', 'empresa', 'D', 'BRL', 0.0,0.0,'','','','2020-01-01','2020-01-01'),
		   (8,'NOME', 74951867, 'N6j7y7a5', 'METATARDER 5', 'server', 'empresa', 'D', 'BRL', 0.0,0.0,'','','','2020-01-01','2020-01-01'),
		   (9,'NOME', 84951867, 'N6j7y7a5', 'METATARDER 5', 'server', 'empresa', 'D', 'BRL', 0.0,0.0,'','','','2020-01-01','2020-01-01'),
		   (10,'NOME', 94951867, 'N6j7y7a5', 'METATARDER 5', 'server', 'empresa', 'D', 'BRL', 0.0,0.0,'','','','2020-01-01','2020-01-01');

INSERT INTO blog_robos(id,nome, descricao, "dataUltUp", version, created, updated, status)
	VALUES (1,'ROBO002', 'ROBO B3', '2022-03-07', 1005, '2022-03-07', '2022-03-07', 'A'),
           (2,'ROBO003', 'Envio de ordens', '2022-03-07', 1006, '2022-03-07', '2022-03-07', 'A'),
           (3,'ROBO004', 'Monitoramento ordens', '2022-03-07', 1007, '2022-03-07', '2022-03-07', 'A');

INSERT INTO blog_configuracoes("urlPrincipal", "dataConf", "loteWin", "loteWdo", "loteB3", "gainDiario", "lossDiario", "lossWin", "gainWin", "lossWdo", "gainWdo", "lossB3", "gainB3", "seguranca","segurancaWDO", created, updated, corretora_id_id, robo_id_id)
	VALUES ('http://serene-beach-09990.herokuapp.com/', '2022-03-07', 1, 1, 10, 30.0,  -60.0,600, 120,   5,  5, 10, 20,200,3, '2022-03-07', '2022-03-07', 1, 2),
	('http://serene-beach-09990.herokuapp.com/'       , '2022-03-07', 1, 1, 10, 50.0,  -100.0,500, 150, 10, 10, 10, 20,100,5, '2022-03-07', '2022-03-07', 2, 2),
	('http://serene-beach-09990.herokuapp.com/'       , '2022-03-07', 1, 1, 10, 75.0,  -150.0,700, 180,  7, 07, 10, 20,150,2, '2022-03-07', '2022-03-07', 3, 2),
	('http://serene-beach-09990.herokuapp.com/'       , '2022-03-07', 1, 1, 10,100.0,  -200.0,800, 200, 12, 12, 10, 20,250,5, '2022-03-07', '2022-03-07', 4, 2),
	('http://serene-beach-09990.herokuapp.com/'       , '2022-03-07', 1, 1, 10, 25.0,  -130.0,900, 225, 15, 15, 10, 20,150,5, '2022-03-07', '2022-03-07', 5, 2),
	('http://serene-beach-09990.herokuapp.com/'       , '2022-03-07', 1, 1, 10, 15.0,  -50.0,555, 250,  20, 20, 10, 20,120,7, '2022-03-07', '2022-03-07', 6, 2),
	('http://serene-beach-09990.herokuapp.com/'       , '2022-03-07', 1, 1, 10, 10.0,  -50.0,200, 300,   8, 08, 10, 20,50 ,4, '2022-03-07', '2022-03-07', 7, 2),
	('http://serene-beach-09990.herokuapp.com/'       , '2022-03-07', 1, 1, 10, 125.0, -125.0,300, 350, 11, 11, 10, 20,150,5, '2022-03-07', '2022-03-07', 8, 2),
	('http://serene-beach-09990.herokuapp.com/'       , '2022-03-07', 1, 1, 10, 150.0, -150.0,400, 400,  6, 12, 10, 20,200,3, '2022-03-07', '2022-03-07', 9, 2),
	('http://serene-beach-09990.herokuapp.com/'       , '2022-03-07', 1, 1, 10, 175.0, -175.0,450, 500, 10, 20, 10, 20,225,5, '2022-03-07', '2022-03-07', 10, 2);
	

INSERT INTO blog_estrategias(
	id, nome, descricao, status, created, updated, isteste)
	VALUES (1, 'FIBONACCI 2', 'FIBONACCI 2', 'A', '2022-03-07', '2022-03-07', 'N'),
		   (2, 'BANDAS DE BOOLLING', 'BANDAS DE BOOLLING', 'A', '2022-03-07', '2022-03-07', 'N'),
		   (3, 'SCALPER04', 'SCALPER04', 'A', '2022-03-07', '2022-03-07', 'N'),
		   (4, 'TOPOS E FUNDOS', 'TOPOS E FUNDOS', 'A', '2022-03-07', '2022-03-07', 'N'),
		   (5, 'SCALPER02', 'SCALPER02', 'A', '2022-03-07', '2022-03-07', 'N'),
		   (6, 'MEDIA 05x21', 'MEDIA 05x21', 'A', '2022-03-07', '2022-03-07', 'N'),
		   (7, 'ESTOCASTICO LENTO', 'ESTOCASTICO LENTO', 'A', '2022-03-07', '2022-03-07', 'N'),
		   (8, 'ROMPIMENTO MAX/MIN', 'ROMPIMENTO MAX/MIN', 'A', '2022-03-07', '2022-03-07', 'N'),
		   (9, 'PRINCIPE DE NY', 'PRINCIPE DE NY', 'A', '2022-03-07', '2022-03-07', 'N'),
		   (10, 'SPEARMAN RANK', 'SPEARMAN RANK', 'A', '2022-03-07', '2022-03-07', 'N'),
		   (11, 'BITEX ONE', 'BITEX ONE', 'A', '2022-03-07', '2022-03-07', 'N'),
		   (12, 'SCALPER NOVO', 'SCALPER NOVO', 'A', '2022-03-07', '2022-03-07', 'N'),
		   (13, 'SCALPER 001', 'SCALPER 001', 'A', '2022-03-07', '2022-03-07', 'N'),
		   (14, 'SCALPER 003', 'SCALPER 003', 'A', '2022-03-07', '2022-03-07', 'N'),
           (15, 'INDICADOR WIN', 'INDICADOR WIN', 'A', '2022-03-07', '2022-03-07', 'N');
		   (15, 'INDICADOR SCALPER', 'INDICADOR SCALPER', 'A', '2022-03-07', '2022-03-07', 'N');
	
	