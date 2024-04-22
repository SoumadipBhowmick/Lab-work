println("Hello World")
using Plots
using Combinatorics

n_particles=400
r=rand(2,n_particles)
ixr=r[1,:].>0.5
ixl=r[1,:].<=0.5

ids=range(1,n_particles)

plot(r[1,:][ixr],r[2,:][ixr],seriestype=:scatter,mc=:red)
plot!(r[1,:][ixl],r[2,:][ixl],seriestype=:scatter,mc=:blue)

v=zeros(2,n_particles)

v[1,r[1,:].<=0.5].=500
v[1,r[1,:].>0.5].=-500
v

ids_pairs=pairs=collect(Combinatorics.combinations(ids,2))
x_pairs=pairs=vcat([x' for x in collect(Combinatorics.combinations(r[1,:],2))]...)
y_pairs=vcat([x' for x in collect(Combinatorics.combinations(r[2,:],2))]...)
dx_pairs=diff(x_pairs,dims=2)
dy_pairs=diff(y_pairs,dims=2)
d_pairs=sqrt.(dx_pairs.^2 + dy_pairs.^2)

radius=0.06
id_pairs_collide=ids_pairs[1,d_pairs .< radius]

v1=v[:,id_pairs_collide[:,1]]
v2=v[:;id_pairs_collide[:,2]]
r1=r[:,id_pairs_collide[:,1]]
r2=r[:,id_pairs_collide[:,1]]




