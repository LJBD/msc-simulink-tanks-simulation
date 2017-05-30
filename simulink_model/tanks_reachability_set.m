run('tanks_runner');
T = 20;
for fi = 0:.1:2*pi
    for theta = 0:.1:2*pi
        p = [sin(theta)*cos(phi); sin(theta)*sin(phi); cos(theta)];
        simOut = sim('tanks_with_costate_equations_model');
        h1 = h1_towork.Data(:);
        h2 = h2_towork.Data(:);
        h3 = h3_towork.Data(:);
        plot3(h1, h2, h3);
        plot3(h1(end), h2(end), h3(end), 'rx');
        hold on;
    end
end

plot(h10, h20, h30, 'go');
grid;
