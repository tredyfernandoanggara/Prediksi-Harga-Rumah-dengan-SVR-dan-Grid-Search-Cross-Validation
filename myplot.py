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

# Group By Plot
def group_plot(data_group, x, y, title=None):
    num_groups = len(data_group)
    num_rows = (num_groups + 1) // 2  # Memastikan jumlah baris cukup

    figsize_x, figsize_y = 12, 4 * num_rows  # Lebar tetap, tinggi menyesuaikan
    fig, axs = plt.subplots(nrows=num_rows, ncols=2, figsize=(figsize_x, figsize_y))
    axs = axs.flatten()

    # Title
    fig.suptitle(title, fontsize=16, y=1)
    
    # Looping setiap kelompok
    for ax, (key, group) in zip(axs, data_group):
        ax.plot(group[x], group[y], marker='o', linestyle='-')
        ax.set_title(f'{key}', fontsize=12)
        ax.set_xlabel(x)
        ax.set_ylabel(y)

        # Menentukan batas X dan Y secara otomatis
        min_x, max_x = group[x].min(), group[x].max()
        min_y, max_y = group[y].min(), group[y].max()
    
        ax.set_xlim(min_x - 1, max_x + 1)  # Ruang ekstra X
        ax.set_ylim(min_y - 10, max_y + 10)  # Ruang ekstra y

        # Menambahkan teks dengan jarak lebih baik
        for X, Y in zip(group[x], group[y]):
            ax.annotate(f'{Y:.2f}', (X, Y), textcoords="offset points", xytext=(0, 5), ha='center')

    # Menyembunyikan subplot yang tidak terpakai
    for j in range(num_groups, len(axs)):
        fig.delaxes(axs[j])

    plt.tight_layout()
    plt.show()