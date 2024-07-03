from database.DB_connect import DBConnect
from model.album import Album


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAlbums(d):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT a.*, SUM(t.Milliseconds) as totD 
                   FROM album a, track t 
                   WHERE a.AlbumId = t.AlbumId 
                   GROUP BY a.AlbumId 
                   HAVING totD > %s"""

        cursor.execute(query, (d,))

        for row in cursor:
            result.append(Album(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCTROW t.AlbumId a1, t2.AlbumId a2
                   FROM playlisttrack p, track t, playlisttrack p2, track t2
                   WHERE p2.PlaylistId = p.PlaylistId
                   AND p2.TrackId = t2.TrackId 
                   AND p.TrackId = t.TrackId 
                   AND t.AlbumId < t2.AlbumId """

        cursor.execute(query, )

        for row in cursor:
            if row["a1"] in idMap and row["a2"] in idMap:
                result.append((idMap[row["a1"]], idMap[row["a2"]]))

        cursor.close()
        conn.close()
        return result
