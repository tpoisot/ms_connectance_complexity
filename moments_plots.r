library(ggplot2)

n_heads = c('c', 'co', 'm', 'v', 'k', 's', 'e')
s_heads = c('co', 're', 'm', 'v', 'k', 's', 'e', 'mod')

rNiche = read.table('niche.dat')
colnames(rNiche) = n_heads

rSim = read.table('unipartites.dat')
colnames(rSim) = s_heads

rNiche$type = rep('niche', nrow(rNiche))
rSim$type = rep('sim', nrow(rSim))

res = merge(rNiche, rSim, all = TRUE)
res = res[,!(names(res) %in% c('re', 'm', 'c', 'mod'))]

## Following code from here: http://gastonsanchez.wordpress.com/2012/08/27/scatterplot-matrices-with-ggplot/

makePairs <- function(data)
{
  grid <- expand.grid(x = 1:ncol(data), y = 1:ncol(data))
  grid <- subset(grid, x != y)
  all <- do.call("rbind", lapply(1:nrow(grid), function(i) {
    xcol <- grid[i, "x"]
    ycol <- grid[i, "y"]
    data.frame(xvar = names(data)[ycol], yvar = names(data)[xcol],
               x = data[, xcol], y = data[, ycol], data)
  }))
  all$xvar <- factor(all$xvar, levels = names(data))
  all$yvar <- factor(all$yvar, levels = names(data))
  densities <- do.call("rbind", lapply(1:ncol(data), function(i) {
    data.frame(xvar = names(data)[i], yvar = names(data)[i], x = data[, i])
  }))
  list(all=all, densities=densities)
}
 
# expand data frame for pairs plot
gg1 = makePairs(res[,-ncol(res)])
 
# new data frame mega_res
mega_res = data.frame(gg1$all, Type=rep(res$type, length=nrow(gg1$all)))
 
# pairs plot
res_plot = ggplot(mega_res, aes_string(x = "x", y = "y")) +
  facet_grid(xvar ~ yvar, scales = "free") +
  geom_point(aes(colour=Type), na.rm = TRUE, alpha=0.8) +
  stat_density(aes(x = x, y = ..scaled.. * diff(range(x)) + min(x)),
               data = gg1$densities, position = "identity",
               colour = "grey20", geom = "line")

print(res_plot)