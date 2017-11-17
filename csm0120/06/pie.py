import matplotlib.pyplot as plt
from matplotlib import cm # colour map

def make_colours(num_items):
    # We'll need enough colours for all the items.
    # Generate enough numbers between 0 and 1 and choose their colours from colormap Set1.
    colornums = []
    for n in range(num_items):
        colornums.append( n/num_items )
    cs = cm.Set1(colornums)
    return cs

def make_pie_plot(values, labels, cols):
    plt.pie(values, colors=cols)
    plt.axis('equal') # Set aspect ratio to be equal so that pie is drawn as a circle
    plt.legend(labels,loc='center left',bbox_to_anchor=(1,0.5)) # Provide a legend whose 'centre left' is shifted outside the axes 
    plt.title('Proportions of phyla in limpet')

    # Save image - make sure extent of image includes legend, which was shifted outside
    plt.savefig("pie.png", bbox_inches='tight')
    

def main():
    sizes = [38.8, 21.2, 10.5, 7.9, 6.3, 4.6, 4, 2.1, 1, 0.86, 0.69, 0.66, 0.51, 0.43]
    phyla_names = ['Proteobacteria', 'Firmicutes', 'Tenericutes', 'Bacteriodes',
                  'Spirochaetes', 'Fusobacteria', 'Euryarchaeota', 'Remaining phyla',
                  'Thermotogae', 'Cyanobacteria', 'Aquificae', 'Crenarchaeota',
                  'Chlamydiae', 'Actinobacteria']

    # What does this for-loop do?
    descriptions = []
    for i in range(0,len(sizes)):
        descriptions.append( phyla_names[i] + " (" + str(sizes[i]) + "%)" )

    # We need many colours
    num_items = len(sizes)
    cs = make_colours(num_items)

    # Now we're ready to plot
    make_pie_plot(sizes, descriptions, cs)


if __name__ == "__main__":
    main()