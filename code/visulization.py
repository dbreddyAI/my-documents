def plot_pie_radar(df, plt_col_names, ax=None):
    """ Plot pie radar, 
    
    Args:
        df: DataFrame, index is the chart segment
        plt_col_names, list, the col needed to be plotted
    
    Returns:
        ax
    """
    n_row = df.shape[0]

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [i_row / float(n_row) * 2 * pi for i_row in range(n_row)]
    angles += angles[:1] # add angle[0] to end of list

    # Initialise the spider plot
    if ax is None:
        ax = plt.subplot(111, polar=True)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], df.index)

    # Draw ylabels
    #ax.set_rlabel_position(0)
    
    # Plot them
    for col_name in plt_col_names:
        col_values = list(df[col_name].values)
        col_values += col_values[:1]
        #print(angles, col_values)
        ax.plot(angles, col_values, linewidth=1, linestyle='solid', label=col_name)
        ax.fill(angles, col_values, alpha=0.1)
        
    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    #plt.legend()
    return ax 