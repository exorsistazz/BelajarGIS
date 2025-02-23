import shapefile

class Kedua:

    def __init__(self):
        self.kedua = shapefile.Writer('kedua', shapeType = shapefile.POLYGON)
        self.kedua.shapeType
        self.kedua.field('nama_ruangan', 'C')

    #Luthfi Muhammad Nabil - 1174035
    def tanggaBawahKiri(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, -2], [4, -2], [4, 1], [-3, 1], [-3, -2]]])
    
    #Luthfi Muhammad Nabil - 1174035
    def tanggaBawahKanan(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, -2], [29, -2], [29, 1], [22, 1], [22, -2]]])

    #Luthfi Muhammad Nabil - 1174035
    def tanggaAtasKiri(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 40], [4, 40], [4, 43], [-3, 43], [-3, 40]]])
    
    #Luthfi Muhammad Nabil - 1174035
    def tanggaAtasKanan(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 40], [29, 40], [29, 43], [22, 43], [22, 40]]])

    #Luthfi Muhammad Nabil - 1174035
    def tamanKosongTengah(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[7, 11], [19, 11], [19, 30], [7, 30], [7, 11]]])

    #Hagan Rowlenstino - 1174040
    def R213(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[7, 40], [10, 40], [10, 33], [7, 33], [7, 40]]])
        
    #Hagan Rowlenstino - 1174040
    def IRC(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[10, 40], [13, 40], [13, 33], [10, 33], [10, 40]]])

    #Hagan Rowlenstino - 1174040
    def RLabBisnis(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[13, 40], [16, 40], [16, 33], [13, 33], [13, 40]]])

    #Hagan Rowlenstino - 1174040
    def RLabComprehensive(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[16, 40], [19, 40], [19, 33], [16, 33], [16, 40]]])

    #Kevin Natanael Nainggolan-1174059
    def ruang208(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 22], [4, 22], [4, 25], [-3, 25], [-3, 22]]])

    #Kevin Natanael Nainggolan-1174059
    def ruang209(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 25], [4, 25], [4, 28], [-3, 28], [-3, 25]]])

    #Kevin Natanael Nainggolan-1174059
    def ruang210(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 28], [4, 28], [4, 31], [-3, 31], [-3, 28]]])

    #Irvan Rizkiansyah - 1174043
    def ruangan205(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 13], [4, 13], [4, 16], [-3, 16], [-3, 13]]])

    #Irvan Rizkiansyah - 1174043
    def ruangan206(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 16], [4, 16], [4, 19], [-3, 19], [-3, 16]]])

    #Irvan Rizkiansyah - 1174043
    def ruangan207(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 19], [4, 19], [4, 22], [-3, 22], [-3, 19]]])
        
    #Liyana Majdah Rahma - 1174039
    def ruangan201(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 1], [4, 1], [4, 4], [-3, 4], [-3, 1]]])
        
    #Liyana Majdah Rahma - 1174039
    def ruangan202(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 4], [4, 4], [4, 7], [-3, 7], [-3, 4]]])

    #Alit Fajar Kurniawan - 1174057
    def RServer(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 34], [29, 34], [29, 37], [22, 37], [22, 34]]])

    #Alit Fajar Kurniawan - 1174057
    def LabLogistik(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 31], [29, 31], [29, 34], [22, 34], [22, 31]]])

    #Dika Sukma Pradana - 1174050
    def ruangan219(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 25], [29, 25], [29, 31], [22, 31], [22, 25]]])

    #Dika Sukma Pradana - 1174050
    def ruangan220(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 22], [29, 22], [29, 25], [22, 25], [22, 22]]])
		
	#Faisal Najib Abdullah - 1174042
    def toiletdosen(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 38.5], [29, 38.5], [29, 40], [22, 40], [22, 38.5]]])
	
	#Faisal Najib Abdullah - 1174042
    def toiletcowo(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 37], [29, 37], [29, 38.5], [22, 38.5], [22, 37]]])
		
	#Faisal Najib Abdullah - 1174042
    def prodiak(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[7, 1], [19, 1], [19, 8], [7, 8], [7, 1]]])
    
    #Rangga Putra Ramdhani - 1174056
    def ruangan203(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 7], [4, 7], [4, 10], [-3, 10], [-3, 7]]])

    #Rangga Putra Ramdhani - 1174056
    def ruangan204(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 10], [4, 10], [4, 13], [-3, 13], [-3, 10]]])

    #Teddy Gideon Manik - 1174038
    def prodiD3MB(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 7], [29, 7], [29, 10], [22, 10], [22, 7]]])

    #Teddy Gideon Manik - 1174038
    def prodiD3LB(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 1], [29, 1], [29, 7], [22, 7], [22, 1]]])
                
    #Muhammad Afra Faris-1174041
    def ruangan211(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 31], [4, 31], [4, 34], [-3, 34], [-3, 31]]])

    #Muhammad Afra Faris-1174041
    def ruangan212(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 34], [4, 34], [4, 37], [-3, 37], [-3, 34]]])

	#Ichsan Hizman Hardy - 1174034
    def ruangan221(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 19], [29, 19], [29, 22], [22, 22], [22, 19]]])
		
	#Ichsan Hizman Hardy - 1174034
    def ruangan222(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 16], [29, 16], [29, 19], [22, 19], [22, 16]]])
        
    #Pasang fungsi baru diatas close()
    def close(self):
        self.kedua.close()