def make_t_distribution(sample_size, mean, sd):
    t_sample = stats.t.rvs(sample_size - 1, mean, sd, sample_size) # Random t-distribution sample
    sample_mean = np.mean(t_sample) # sample mean
    sample_std = np.std(t_sample) # sample standard deviation
    t_dist = stats.t(df = sample_size - 1, loc = sample_mean, scale = sample_std) # make a t-distribution based on the sample
    x_axis = np.linspace(t_dist.ppf(0.0001), t_dist.ppf(0.9999), 500) # Generate an x-axis based on t-quantile values

    return t_dist, x_axis

def q1_graph():

    fig = plt.figure(figsize=(4,3))
    t_dist_10, x_axis_10 = make_t_distribution(10, 0,2)
    t_dist_100, x_axis_100 = make_t_distribution(100, 0,2)
    t_dist_1000, x_axis_1000 = make_t_distribution(1000, 0,2)
    t_dist_5000, x_axis_5000 = make_t_distribution(5000, 0,2)

    y_axis_10 = t_dist_10.pdf(x_axis_10)
    y_axis_100 = t_dist_100.pdf(x_axis_100)
    y_axis_1000 = t_dist_1000.pdf(x_axis_1000)
    y_axis_5000 = t_dist_5000.pdf(x_axis_5000)

    plt.plot(x_axis_10, y_axis_10,':',linewidth=3) #blue
    plt.plot(x_axis_100, y_axis_100,'--',linewidth=3) #yellow
    plt.plot(x_axis_1000, y_axis_1000,'-.',linewidth=3) #green
    plt.plot(x_axis_5000, y_axis_5000,'--',linewidth=3) #red

    mu = 0
    variance = 1
    sigma = 2
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma), color = 'blue')

    plt.xlim(-6,6)

    return fig

def q1_graph_big():

    fig = plt.figure(figsize=(12,8))
    t_dist_10, x_axis_10 = make_t_distribution(10, 0,2)
    t_dist_100, x_axis_100 = make_t_distribution(100, 0,2)
    t_dist_1000, x_axis_1000 = make_t_distribution(1000, 0,2)
    t_dist_5000, x_axis_5000 = make_t_distribution(5000, 0,2)

    y_axis_10 = t_dist_10.pdf(x_axis_10)
    y_axis_100 = t_dist_100.pdf(x_axis_100)
    y_axis_1000 = t_dist_1000.pdf(x_axis_1000)
    y_axis_5000 = t_dist_5000.pdf(x_axis_5000)

    plt.plot(x_axis_10, y_axis_10,':',linewidth=2) #blue
    plt.plot(x_axis_100, y_axis_100,'--',linewidth=2) #yellow
    plt.plot(x_axis_1000, y_axis_1000,'-.',linewidth=2) #green
    plt.plot(x_axis_5000, y_axis_5000,'--',linewidth=2) #red

    mu = 0
    variance = 1
    sigma = 2
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma), color = 'blue')

    plt.xlim(-6,6)
    plt.legend(x_axis_10, labels = ['t-distribution, n = 10', 't-distribution, n = 100','t-distribution, n = 1000','t-distribution, n = 5000', 'Normal Dist. μ=0, σ=2'])
    plt.xlabel('Standard Deviation')
    plt.ylabel('Probability Density')

    return fig

%%capture out
for x in range(6):
    q1_graph().savefig('q1_graph{}.png'.format(x))
image_list = []
for x in range(6):
    image = Image.open('q1_graph{}.png'.format(x)).convert('RGB')
    image_list.append(image)
big = q1_graph_big().savefig('q1_graph_big.png')
big_image = Image.open('q1_graph_big.png')

#contact sheet
contactsheet = Image.new('RGB', (1700,760),'#D3D3D3')

contactsheet.paste(image_list[0],(1380,30))
contactsheet.paste(image_list[1],(1075,30))
contactsheet.paste(image_list[2],(1380,270))
contactsheet.paste(image_list[3],(1075,270))
contactsheet.paste(image_list[4],(1380,510))
contactsheet.paste(image_list[5],(1075,510))
contactsheet.paste(big_image,(100,150))

draw = ImageDraw.Draw(contactsheet)
text = 'Probabilty Density Plot'
f = ImageFont.truetype('fanwood-webfont.ttf',25)
f2 = ImageFont.truetype('fanwood-webfont.ttf',18)
f3 = ImageFont.truetype('fanwood-webfont.ttf',16)
draw.text((400, 5), text, font = f, fill = 'black')
draw.text((1210,5), 'Plot Examples: Changes in Distribution', font = f2, fill = 'black')
text2 = """
As sample sizes increase, the sampling distributions approach a normal distribution. With sample size increase, the variability of each sampling distribution decreases
so that they become increasingly more leptokurtic.Shown in the density plot below, and to the right, sample sizes 10 and 100 have more variability. Sample sizes
1000, and 5,000 more closely resemble a normal distribution of scores. This is why a large sample size is important factor if to articulate performance issues.
"""
draw.text((40, 30), text2, font = f3, fill='black', align = 'center')


contactsheet
