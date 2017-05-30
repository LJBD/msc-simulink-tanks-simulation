run('tanks_runner');

for fi = 0:.1:2*pi
    for theta = 0:.1:2*pi
        p = [sin(theta)*cos(phi); sin(theta)*sin(phi); cos(theta)];
        simOut = sim('tanks_with_costate_equations_model');
        h1 = h1_towork.Data(:);
        h2 = h2_towork.Data(:);
        plot(h1, h2);
        plot(h1(end), h2(end), 'rx');
        hold on;
    end
end