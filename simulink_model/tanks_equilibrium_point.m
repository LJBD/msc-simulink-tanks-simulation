function [ h_eq ] = tanks_equilibrium_point( C, u )
%tanks_equilibrium_point - return a point of equilibrium for tanks
%   Detailed explanation goes here
    h_eq = zeros(3, 1)
    C_squared = C.^2;
    h_eq(1) = C_squared(1) * u.^2
    h_eq(2) = C_squared(1).^2 / C_squared(2) * u.^2
    h_eq(3) = C_squared(1).^2 / C_squared(3) * u.^2
end

