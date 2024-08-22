class Door:
    """
    Diese Klasse beschreibt eine Tür mit der Eigenschaft color (Farbe) und den Zuständen
    door_is_open (für geöffnete Tür) sowie door_is_locked (für verriegelte Tür).
    Die Tür überwacht die beiden Zustände und verhindert so Aktionen, die nicht möglich sind.
    Das Verriegeln delegiert die Tür an ein Objekt vom Typ DoorLock (Türschloss).
    """

    def __init__(self, ref2door_lock, base_color):
        """
        Erzeugt ein Tür-Objekt.
        :param ref2door_lock: Referenz auf ein DoorLock-Objekt
        :param base_color: Die Farbe der Tür
        """
        self._the_door_lock = ref2door_lock
        self.color = base_color
        self._door_is_open = False
        self._door_is_locked = False

    def open_the_door(self):
        """
        Methode für das Öffnen der Tür.
        Das ist nur möglich, wenn die Tür nicht verriegelt ist.
        """
        if not self._door_is_locked:
            self._door_is_open = True

    def close_the_door(self):
        """
        Methode für das Schließen der Tür.
        Das geht immer, auch wenn die Tür schon geschlossen oder verriegelt ist.
        """
        self._door_is_open = False

    def lock_the_door(self):
        """
        Methode für das Verriegeln der Tür.
        Das ist nur möglich, wenn die Tür nicht offen ist.
        Für das Verriegeln ist das Türschloss zuständig.
        """
        if not self._door_is_open:
            self._door_is_locked = self._the_door_lock.lock()

    def unlock_the_door(self):
        """
        Methode für das Entriegeln der Tür.
        Das ist nur möglich, wenn die Tür verriegelt ist.
        Für das Entriegeln ist das Türschloss zuständig.
        """
        if self._door_is_locked:
            self._door_is_locked = not self._the_door_lock.unlock()

    def test(self):
        """
        Gibt den Zustand aller Attribute der Tür aus.
        """
        print(f'Türfarbe: {self.color}')
        print(f'Tür offen: {"Ja" if self._door_is_open else "Nein"}')
        print(f'Tür verriegelt: {"Ja" if self._door_is_locked else "Nein"}')

    @property
    def door_is_open(self):
        """
        Getter-Methode für den Zustand door_is_open.
        :return: True, wenn die Tür offen ist, sonst False
        """
        return self._door_is_open

    @property
    def door_is_locked(self):
        """
        Getter-Methode für den Zustand door_is_locked.
        :return: True, wenn die Tür verriegelt ist, sonst False
        """
        return self._door_is_locked

    @property
    def color(self):
        """
        Getter-Methode für die Eigenschaft color.
        :return: Die Farbe der Tür
        """
        return self._color

    @color.setter
    def color(self, new_color):
        """
        Setter-Methode für die Eigenschaft color.
        :param new_color: Die neue Farbe der Tür
        """
        self._color = new_color


class DoorLock:
    """
    Dummy-Klasse für ein Türschloss, damit die Klasse Door funktioniert.
    """

    def __init__(self):
        print("Ein Schloss wurde erzeugt.")

    def lock(self):
        """
        Verriegelt das Schloss.
        :return: True, wenn das Schloss verriegelt wurde.
        """
        return True

    def unlock(self):
        """
        Entriegelt das Schloss.
        :return: False, wenn das Schloss entriegelt wurde.
        """
        return False


# Main-Methode zum Testen
if __name__ == "__main__":
    print("Test für Tür-Objekt")
    the_door_lock = DoorLock()
    the_door = Door(the_door_lock, "grün")
    the_door.test()

    print("-- Türe jetzt öffnen --")
    the_door.open_the_door()
    the_door.test()

    print("-- Türe jetzt schließen --")
    the_door.close_the_door()
    the_door.test()

    print("-- Türe jetzt verriegeln --")
    the_door.lock_the_door()
    the_door.test()

    print("-- Türe jetzt entriegeln --")
    the_door.unlock_the_door()
    the_door.test()
