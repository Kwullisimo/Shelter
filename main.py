from menu import create_shelter, Menu

# ==================== 
# =======MAIN=========
# ====================

def main():
    shelter = create_shelter()
    Menu(shelter).run()

if __name__ == "__main__":
    main()