# Esse código pega os resultados da simulação e os converte em uma camada raster que pode ser visualizada no QGIS.
from qgis.core import QgsRasterLayer, QgsProject
import numpy as np
from osgeo import gdal

def create_output_layer(h, L, dx):
    # Este método cria uma camada raster (imagem) no QGIS para exibir os resultados da simulação.
    # Parâmetros:
    # h: lista dos valores do nível de água
    # L: comprimento da área simulada
    # dx: resolução espacial (distância entre os pontos)
    
    n = len(h)  # Número de pontos
    cols = int(L / dx)  # Número de colunas na camada raster (baseado no comprimento total)
    rows = 1  # Uma linha, pois estamos simulando em 1D

    # Cria uma matriz numpy com os valores de 'h' para gerar a imagem raster
    raster_data = np.zeros((rows, cols))
    raster_data[0, :] = h

    # Configurações para criar o arquivo raster
    driver = gdal.GetDriverByName('GTiff')
    output_path = "output.tif"
    out_raster = driver.Create(output_path, cols, rows, 1, gdal.GDT_Float32)
    out_raster.SetGeoTransform((0, dx, 0, 0, 0, -dx))  # Define a localização geográfica do raster
    out_band = out_raster.GetRasterBand(1)
    out_band.WriteArray(raster_data)
    out_band.FlushCache()
    out_raster = None  # Fecha o arquivo para salvá-lo

    # Adiciona a camada raster ao QGIS
    layer = QgsRasterLayer(output_path, 'Simulação de Nível do Lençol Freático')
    if not layer.isValid():
        raise Exception("Erro ao criar a camada raster.")
    QgsProject.instance().addMapLayer(layer)