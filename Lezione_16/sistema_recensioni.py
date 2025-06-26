class Media:

    _title: str
    _reviews: list[int]

    def __init__(self, title: str, reviews: list[int]) -> None:
        
        self._set_title(title)
        self._reviews = reviews




    def _set_title(self, title: str) -> None:

        self._title = title

    def get_title(self) -> str:

        return self._title
    
    def aggiungiValutazione(self, voto: int) -> None:

        if 1 <= voto <= 5:

            self._reviews.append(voto)

        else:
            raise ValueError("Il voto deve essere compreso tra 1 e 5")
        
    def _getMedia(self) -> float:

        if not self._reviews:

            raise RuntimeError("Questo film non ha reviews, non si può calcolare la media")
        
        else:

            somma: int = 0

            for v in self._reviews:
                somma += v
            
            media: float = somma / len(self._reviews)

            return round(media, 2)
        
    def _getRate(self) -> str:

        media_arr: int = round(self._getMedia(), 0)

        match media_arr:

            case 1:
                return "Terribile"
            
            case 2:
                return "Brutto"
            
            case 3:
                return "Normale"
            
            case 4:
                return "Bello"
            
            case 5:
                return "Grandioso"
            
    def _ratePercentage(self, voto: int) -> int:

        n_voti: int = 0

        for v in self._reviews:
            if v == voto:
                n_voti += 1

        percentage: int = round(((n_voti * 100) / len(self._reviews)), 2)

        return percentage
    
    def recensione(self) -> None:

        print(f"\
            Titolo del Film: {self.get_title()}\n\
            Voto Medio: {self._getMedia()}\n\
            Giudizio: {self._getRate()}\n\
            Terribile: {self._ratePercentage(1)}%\n\
            Brutto: {self._ratePercentage(2)}%\n\
            Normale: {self._ratePercentage(3)}%\n\
            Bello: {self._ratePercentage(4)}%\n\
            Grandioso: {self._ratePercentage(5)}%")
        
class Film(Media):
    
    def __init__(self, title, reviews):
        super().__init__(title, reviews)


if __name__ == "__main__":

    a: Film = Film("Fuga da Alcatraz", [])
    b: Film = Film("Boh", [])

    a.aggiungiValutazione((3))
    a.aggiungiValutazione((4))
    a.aggiungiValutazione((3))
    a.aggiungiValutazione((1))
    a.aggiungiValutazione((5))
    a.aggiungiValutazione((4))
    a.aggiungiValutazione((4))
    a.aggiungiValutazione((2))
    a.aggiungiValutazione((5))
    a.aggiungiValutazione((3))
    a.aggiungiValutazione((4))

    b.aggiungiValutazione((2))
    b.aggiungiValutazione((4))
    b.aggiungiValutazione((2))
    b.aggiungiValutazione((2))
    b.aggiungiValutazione((1))
    b.aggiungiValutazione((3))
    b.aggiungiValutazione((1))
    b.aggiungiValutazione((3))
    b.aggiungiValutazione((5))
    b.aggiungiValutazione((4))
    b.aggiungiValutazione((2))
    b.aggiungiValutazione((3))

    a.recensione()
    print("-------------------------------------")
    b.recensione()


        
    
