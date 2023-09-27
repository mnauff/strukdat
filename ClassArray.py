########################################
# ArrayADT
#######################################
class ClassArray:
    # Deklarasi Array Default 100
    def __init__(self, PanjangArray=100):

        self.Value = [0] * PanjangArray
        self.TopIndex = -1  # Berisi Index tertitinggi yang berisi data ,Default -1
        # Index Tertinggi yang dapat digunakan untuk menyimpan data
        self.MaxIndex = PanjangArray-1

       ##########################################
       # Implementasi Fungsi dalam array ADT
       #########################################

       # 1. Fungsi Menambah Data
    def Append(self, Value):
        # Mendambahkan Suatu nilai ke array apabila TopIndex <MaxIndex
        if self.TopIndex < self.MaxIndex:
            # Update TopIndex
            self.TopIndex = self.TopIndex+1
            self.Value[self.TopIndex] = Value
    # 2. Fungsi Transversal

    def Cetak(self):
        # Operasi Transversal Untuk mencetak seluruh nilai yang tersipan pada array
        for i in range(self.TopIndex+1):
            print("Value[", i, "]=", self.Value[i])

    # 3. Fungsi Insert
    def Insert(self, InsertIndex, Value):
        if InsertIndex > self.TopIndex:
            return
        self.TopIndex = self.TopIndex + 1
        if self.TopIndex >= self.MaxIndex:
            self.TopIndex = self.MaxIndex
        # Menggeser Isi Element dari TopIndex sampai ke Insert Index
        for i in range(self.TopIndex, InsertIndex, -1):
            self.Value[i] = self.Value[i-1]
        self.Value[InsertIndex] = Value

    # 4. Fungsi Menghapus Item pada index tertentu
    def Delete(self, DeleteIndex):
        # Menghapus elemt array pada Posisi NoIndex
        if DeleteIndex > self.MaxIndex:
            return
        # Menggeser isi dari item
        for i in range(DeleteIndex, self.TopIndex):
            self.Value[i] = self.Value[i+1]
        if self.TopIndex >= 0:
            self.TopIndex = self.TopIndex - 1
    # 5. Fungsi Edit Value Pada Index tertentu

    def Edit(self, NoIndex, Value):
        if NoIndex > self.TopIndex:
            return
        self.Value[NoIndex] = Value

    # 6. Mencari Index Array dari suatu Nilai Tertentu
    def Search(self, Value):
        SearchIndex = -1

        for i in range(self.TopIndex):
            if self.Value[i] == Value:
                # Nilai yang yang dicari ditemukan dalam array
                # Update variabel SearchIndex sesuai dengan posisi nilai yang ditemukan
                self.SearchIndex = i
                break
        return SearchIndex

    def RemoveElement(self, element):
        i = 0
        while i <= self.TopIndex:
            if self.Value[i] == element:
                # Shift elements to the left to remove the element
                for j in range(i, self.TopIndex):
                    self.Value[j] = self.Value[j+1]
                self.TopIndex -= 1  # Decrease the top index
            else:
                i += 1

#########################################
# Program Utama
#########################################


# Mendeklarasikan Array dengan Jumlah elemen 100
c = ClassArray(100)
print("Menambah enam buah elemen ke array")

c.Append(1)
c.Append(2)
c.Append(3)
c.Append(4)
c.Append(5)
c.Append(6)
# Mencetak array
c.Cetak()
print("Menyisipkan Nilai -1 pada elemen array dengan index 4")
c.Insert(4, -1)
# Mencetak Array
c.Cetak()
# print("Menghapus elemen pada posisi ke 4")
# c.Delete(4)

# c.Cetak()
# print("Mengganti Nilai dari elemen ke 4 dengan -5")
# c.Edit(4, -5)
# c.Cetak()

# c.Cetak()
print("Menghapus elemen 2")
c.RemoveElement(2)
c.Cetak()
