import matplotlib.pyplot as plt
import seaborn as sns

# Barplot
def bar_plot(x, y, hue=None, title=None):
    ax = sns.barplot(x=x, y=y, hue=hue)
    
    for p in ax.patches:
        # Mendapatkan teks
        text = p.get_height()
        
        if p.xy != (0, 0):
            # Annotate text
            ax.text(x=p.get_x() + p.get_width() / 2, y=p.get_height(),
                    s=text,
                    ha='center', va='bottom', fontsize=10, color='black')
    # Title
    plt.title(title)
    # Layout
    plt.tight_layout()
    plt.show()

# Regresi Plot
def reg_plot(data, x, y, title=None):
    sns.regplot(data=data, x=x, y=y)

    plt.title(title)
    plt.grid()
    plt.tight_layout()
    plt.show()